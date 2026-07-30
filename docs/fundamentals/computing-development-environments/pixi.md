# Pixi: The evolution of cross-platform package manager

Pixi is a fast, project-centric package manager that combines the conda-forge and PyPI ecosystems behind a single manifest and a single lock file, giving you the same environment on every machine without a separate activation step.

!!! info "Version"

    Verified against pixi 0.73.0 (July 2026). Commands and output on this page
    were captured from a real run against that version. Older pixi releases may
    differ; where a feature needs a minimum version, it is noted inline.

## Why pixi?

You inherit a project. It has an `environment.yml` or a `requirements.txt` sitting at the top level, so you do what the README says: create the environment and run the analysis. Sometimes the solve just fails — a pinned version no longer exists on the channel, or a new release broke a transitive dependency that used to resolve cleanly. Other times it's worse: the solve succeeds, the environment builds, and you get numbers that don't match the paper.

This is not bad luck. It's the default outcome. Neither conda nor pip writes a lock file unless you go out of your way to produce one — `conda env export`, `pip freeze` — and most projects don't. An `environment.yml` or `requirements.txt` describes an *intent* ("something compatible with numpy>=1.20"), not a record of what was actually installed. Solve that intent again six months later, against a channel that has moved on, and you can easily land on a different set of package versions.

Named conda environments compound the problem. A `conda create -n myenv` environment is shared and long-lived: it sits outside the project, gets `conda install`ed into over months, and nobody remembers exactly what's in it anymore. Whether it's even active is invisible state that lives in your shell, not in the project directory — you can `cd` into a project and have no idea if the right environment, or any environment, is active.

For the rest of this page, "reproducible" means one specific thing: **same inputs plus the same environment yields the same outputs, on anyone's machine.** Everything pixi does is in service of that definition.

### The conda workflow

![Conda Workflow](../../assets/images/conda-workflow.png)

The typical "best practice" conda workflow has three separate processes, each involving the same environment file:

- **New environment** — write a `environment.yml`, create the environment from it, then activate it before you can work.
- **Update** — edit the `environment.yml`, update the environment from the changed file, then reactivate.
- **Share** — hand the `environment.yml` to a collaborator and hope their solve matches yours.

Every step depends on a human remembering to keep the environment and the file in sync, and none of the steps produce an exact, replayable record of what got installed. See [Conda/Mamba Fundamentals](./conda-mamba.md) for the full conda workflow.

### conda/mamba, uv, and pixi

| Concern | conda / mamba | uv | pixi |
| --- | --- | --- | --- |
| Environment scope | Shared, named, global | Per-project | Per-project, tied to the folder |
| Lock file | Opt-in (`conda env export`) | Yes, by default | Yes, written automatically on every change |
| Task running | None | None | Built in (`pixi run <task>`) |
| Activation | `conda activate` required | Not required | Never required |
| conda-forge packages | Yes | No | Yes |
| PyPI packages | Via nested `pip:` | Yes | Yes, same manifest and lock |
| Compiled/system libs (CUDA, MKL, GDAL) | Yes | Only if a wheel exists | Yes |

!!! tip "When `uv` alone is enough"

    For a pure-Python project whose dependencies all live on PyPI, `uv` is an
    excellent choice and you do not need pixi. Pixi earns its place when your
    stack includes compiled or non-Python dependencies — the Python interpreter
    itself, CUDA, MKL, GDAL's C libraries — that either are not on PyPI or ship
    there as fragile wheels.

??? info "How pixi actually solves an environment"

    Pixi does not compete with `uv` so much as build on it. When pixi solves an
    environment it resolves the **conda** packages first with the `rattler`
    solver, then resolves the **PyPI** packages with `uv` — and crucially, it
    resolves the PyPI half *on top of* the conda half, so the two are guaranteed
    compatible. Both are driven by the same SAT solver, `resolvo`, and both land
    in a single `pixi.lock`.

    That is the real difference in scope: `uv` resolves PyPI. Pixi resolves
    conda-forge *and* PyPI, together, in one lock file.

## Installation

### Quick Installation (Recommended)

On Linux & macOS, you can install pixi by running the following command:

```bash
# With curl
curl -fsSL https://pixi.sh/install.sh | bash

# Or with wget
wget -qO- https://pixi.sh/install.sh | sh
```

On Windows you can download the [installer](https://github.com/prefix-dev/pixi/releases/latest/download/pixi-x86_64-pc-windows-msvc.msi) or run the following command:

```powershell
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

For other installation methods go the the [pixi installation docs](https://pixi.sh/latest/installation/).

### Verification

Once you have pixi installed, you can verify by running the command below

```bash
pixi --version
```

## Your first project

Create a new project with `pixi init`, then move into it:

```bash
pixi init my-analysis
cd my-analysis
```

pixi creates a small tree:

```text
my-analysis/
├── .gitattributes
├── .gitignore
└── pixi.toml
```

`pixi.toml` is the manifest — the file you edit by hand to describe the project. This is exactly what `pixi init` writes into it:

```toml title="pixi.toml"
[workspace]
channels = ["conda-forge"]  # (1)!
name = "my-analysis"  # (2)!
platforms = ["osx-arm64"]  # (3)!
version = "0.1.0"  # (4)!

[tasks]

[dependencies]
```

1. `channels` says where packages come from, in priority order. `conda-forge` is the default.
2. `name` identifies the project. `pixi init` took it from the argument you gave it.
3. `platforms` says which platform(s) the lock file must cover. Add more (`linux-64`, `win-64`, `linux-aarch64`, ...) so the project also solves on other machines.
4. `version` is the project's own version, independent of anything you later publish.

`[tasks]` and `[dependencies]` are generated empty — pixi always writes both tables, ready for you to fill in as you add tasks and packages later in this guide.

`authors` and `description` are optional fields you can add yourself; pixi 0.73.0's `init` does not write them, however you may see them listed in older tutorials.

!!! note "`[workspace]` or `[project]`?"

    Older pixi tutorials show a `[project]` table. It was renamed to
    `[workspace]`. `[project]` still parses, but pixi 0.73.0 emits a deprecation
    warning telling you to replace it. Use `[workspace]` in new projects.

### Adding dependencies

A project with no dependencies doesn't do much. Add the three packages this analysis needs:

```bash
pixi add python numpy matplotlib
```

```text
✔ Added python >=3.14.6,<3.15
✔ Added numpy >=2.5.1,<3
✔ Added matplotlib >=3.11.1,<4
```

Notice that `python` went in unpinned — the command was `pixi add python`, not `pixi add python=3.11`. pixi's default pinning strategy already wrote the `>=3.14.6,<3.15` range for you, so you rarely need to pin versions by hand.

`pixi.toml` now has a filled-in `[dependencies]` table:

```toml title="pixi.toml"
[dependencies]
python = ">=3.14.6,<3.15"
numpy = ">=2.5.1,<3"
matplotlib = ">=3.11.1,<4"
```

## What just happened

Look at the directory again:

```text
my-analysis/
├── .gitattributes
├── .gitignore
├── .pixi/
├── pixi.lock
└── pixi.toml
```

Two new things appeared: `pixi.lock` and `.pixi/`. Their sizes on disk tell you most of what you need to know about what each one is for:

```text
      12 pixi.toml
    1184 pixi.lock
```

`pixi.toml` barely grew — it's still three short version ranges. `pixi.lock` is nearly a hundred times larger. That gap is the whole model:

- **`pixi.toml` is the manifest: your intent.** Version ranges, written by you, small and readable, meant to be reviewed in a diff.
- **`pixi.lock` is the lock file: the exact solution.** Every package, every exact version, build string and hash, resolved for every platform listed in `platforms`. pixi writes and maintains it; you never hand-edit it.
- **`.pixi/` is the environment directory: a disposable build product.** It's the actual environment — interpreter and packages unpacked on disk — built from `pixi.lock`. It's gitignored, and pixi can rebuild it from the lock file at any time.

Commit `pixi.toml` and `pixi.lock`. Never commit `.pixi/`.
