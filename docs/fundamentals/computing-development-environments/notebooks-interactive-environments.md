# Notebooks and Interactive Environments

Jupyter notebooks are how a lot of research code starts. You load some data, plot it, adjust something, plot it again, and the record of that exploration is the notebook itself. That tight loop is the right tool for figuring out what your data looks like.

The properties that make a notebook good for exploring are the same ones that make it hard to hand to somebody else and get the same numbers back. This page is about the practices that close that gap.

!!! note "This page is Python-focused"

    Jupyter itself is language-agnostic, but `ipykernel`, `nbval`, and
    papermill's parameter handling below are all shown in their Python form.
    The version control and hidden-state sections apply to any kernel.

## The kernel is the environment

A notebook does not contain a Python installation. It sends code to a **kernel**, a separate process running in some environment, and displays whatever comes back. The notebook file records which kernel it wants in its metadata:

```json
"kernelspec": {
  "display_name": "Python 3",
  "language": "python",
  "name": "python3"
}
```

That is a name. Nothing in it pins a package version. If a colleague's notebook throws `ModuleNotFoundError` on your machine when it clearly ran on theirs, this is usually why: you have the notebook and not their environment.

So the first thing to get right is the same thing the rest of this chapter is about. Create a project environment with [Pixi](./pixi.md) or [conda/mamba](./conda-mamba.md), install `ipykernel` into it, and launch Jupyter from inside it. To see which kernels Jupyter can actually find:

```bash
jupyter kernelspec list
```

```text
Available kernels:
  python3    /Users/you/projects/glacier-melt/.pixi/envs/default/share/jupyter/kernels/python3
```

Check that path. Pointing at a kernel from a different environment than the one you think you are in is the first thing we check when someone's notebook will not run.

!!! tip "Register a project environment as a named kernel"

    If you run one Jupyter installation and want to switch between project
    environments from the kernel picker, install a named kernel from inside each
    environment:

    ```bash
    python -m ipykernel install --user --name my-project --display-name "My Project"
    ```

    Launching Jupyter from within the project environment is simpler where you
    can do it, because the kernel cannot then drift from the environment that
    defines it.

## Hidden state

The order the cells are written in and the order they were actually run in are different things. `execution_count` records the second one.

Here is a notebook that looks healthy:

```python
import numpy as np
rng = np.random.default_rng(0)
```

```python
samples = rng.random(1000)
print(f"mean: {samples.mean():.4f}")
```

```text
mean: 0.4998
```

```python
print(f"scaled mean: {(samples * scale).mean():.4f}")
```

```text
scaled mean: 4.9980
```

Every cell has stored output and none shows an error. Now run it top to bottom in a fresh kernel:

```bash
jupyter execute analysis.ipynb
```

```text
NameError: name 'scale' is not defined
```

`scale` was defined in a cell that got deleted at some point after it ran. The value survived in the kernel's memory, so every subsequent run kept working, and the saved output records a result the notebook can no longer produce. Nothing about the file looks wrong. It simply cannot be re-run.

That failure mode is silent, and it survives being committed, shared, and cited.

The habit that prevents it costs nothing: **restart the kernel and run all cells before you commit or share anything.** In JupyterLab that is Kernel then Restart Kernel and Run All Cells; in VS Code it is the Restart button followed by Run All. If it does not survive that, it is not finished, whatever the stored outputs say.

## Notebooks in version control

`.ipynb` files are JSON, so Git technically handles them. It just does not handle them well.

Change one number in one line of code and commit. These are the changed lines:

```diff
-   "execution_count": 1,
+   "execution_count": 7,
-      "0.5169\n"
+      "0.5023\n"
-    "print(f\"{rng.random(1000).mean():.4f}\")"
+    "print(f\"{rng.random(2000).mean():.4f}\")"
```

One logical change, three changed lines, two of them bookkeeping nobody wants to review. Re-running a notebook without editing it at all still produces a diff, because every `execution_count` bumps.

Outputs are the bigger problem. A notebook containing a single matplotlib plot stores that image as base64 text inside the JSON. In a small test notebook, one plot came to 42,884 characters, taking the file from 446 bytes to 44,440. Those blobs change completely whenever the figure is regenerated, so a rendering difference no human can see registers as tens of thousands of changed characters. Repeat that across a few notebooks and code review stops happening.

### Diff and merge notebooks properly

[nbdime](https://nbdime.readthedocs.io/) diffs notebooks as notebooks rather than as JSON. `nbdiff -s` restricts the comparison to source:

```bash
nbdiff -s analysis.ipynb
```

```text
## modified /cells/0/source:
@@ -1,3 +1,3 @@
 import numpy as np
 rng = np.random.default_rng(0)
-print(f"{rng.random(1000).mean():.4f}")
+print(f"{rng.random(2000).mean():.4f}")
```

Wire it into Git so `git diff` uses it for `.ipynb` files:

```bash
nbdime config-git --enable
```

nbdime also ships `nbmerge` and `nbdiff-web`. That matters more than the diff, because a merge conflict inside notebook JSON is close to unresolvable by hand: Git puts conflict markers in the middle of a JSON structure and the result is not a valid notebook. Stripping outputs makes conflicts rarer without helping you resolve the ones you still get.

### Strip outputs on commit

[`nbstripout`](https://github.com/kynan/nbstripout) removes outputs and execution counts as files are staged, leaving your working copy untouched:

```bash
nbstripout --install
```

It writes the attribute lines to `.git/info/attributes`:

```text
*.ipynb filter=nbstripout
*.ipynb diff=ipynb
```

After that, bumping `execution_count` from 1 to 99 and rewriting the stored output leaves `git diff` nothing to report. Only source changes show up.

There are two reasons to do this and the second one is the one people underrate. Review friction is the obvious one. The other is that **outputs leak**: API tokens printed from a config cell, absolute paths carrying your username, query results, subject-level data. Once that is committed it stays in the history, and so does the base64 bloat, neither of which comes out without rewriting history.

Against that, stripped notebooks reach a reader with no outputs, so the rendered plots are gone from GitHub's preview. For a repository whose notebooks are meant to be read rather than run, committing outputs may be the right call.

!!! warning "`--install` does not travel with the repository"

    `nbstripout --install` writes attributes to `.git/info/attributes` and the
    filter driver itself to `.git/config`. Neither is tracked, so every
    collaborator has to run it after cloning.

    Committing a `.gitattributes` with `*.ipynb filter=nbstripout` is not enough
    on its own. Without the driver defined, Git silently passes the content
    through unchanged and the outputs land in the commit anyway. The fix that
    does travel is the [nbstripout pre-commit hook](https://github.com/kynan/nbstripout#using-nbstripout-as-a-pre-commit-hook),
    configured in `.pre-commit-config.yaml`.

### Pair with a text file

[Jupytext](https://jupytext.readthedocs.io/) can pair a notebook with a plain script and keep the two in sync:

```bash
jupytext --set-formats ipynb,py:percent analysis.ipynb
```

```python title="analysis.py"
# %%
import numpy as np
rng = np.random.default_rng(0)

# %%
samples = rng.random(1000)
print(f"mean: {samples.mean():.4f}")
```

The `# %%` markers are cell boundaries, and both VS Code and PyCharm treat that format as a runnable notebook. Commit the `.py`, gitignore the `.ipynb`, and code review becomes ordinary Python review.

Pairing is what keeps the two files together: `--set-formats` records the pairing in the notebook's metadata, and Jupyter updates both on save once the Jupytext extension is installed. Outside Jupyter, `jupytext --sync analysis.ipynb` reconciles them. A bare `jupytext --to py:percent` is a one-way export, which is fine for a snapshot and will silently go stale if you keep editing the notebook.

## Running a notebook without opening it

`jupyter execute` runs a notebook end to end and exits non-zero if any cell raises, which makes it usable in CI as a smoke test:

```bash
jupyter execute analysis.ipynb
```

To keep the executed copy, use nbconvert instead:

```bash
jupyter nbconvert --to notebook --execute analysis.ipynb --output run-2026-08-11.ipynb
```

[Papermill](https://papermill.readthedocs.io/) parameterises the notebook. Tag one cell `parameters` in its cell metadata, and Papermill injects overrides beneath it at runtime:

```bash
papermill analysis.ipynb out.ipynb -p n_samples 5000 -p seed 42
```

The executed notebook records what it was given, as an injected cell:

```python
# Parameters
n_samples = 5000
seed = 42
```

```text
n=5000 seed=42 mean=0.4956
```

That output notebook carries the parameters, the code, and the results together, which makes it worth archiving per run. If the run is one you will cite, archive the environment lock file alongside it and mint a DOI with [Zenodo](https://zenodo.org/).

## Testing a notebook

If a notebook's stored outputs are supposed to be correct, [`nbval`](https://nbval.readthedocs.io/) holds them to it. It re-executes each cell and compares against what is saved:

```bash
pytest --nbval analysis.ipynb
```

```text
1 passed in 0.89s
```

When reality and the stored output disagree it says so precisely:

```text
  '0.5000\n' == '0.5169\n'
  - 0.5169
  + 0.5000
FAILED analysis.ipynb::Cell 0
```

Be careful what you point this at. Anything with a timestamp, an unseeded random draw, a file path, or a `<matplotlib.figure.Figure at 0x...>` repr fails on every run for reasons unrelated to your code. Two flags handle that. `--nbval-lax` still executes every cell but only compares output for cells you mark with `# NBVAL_CHECK_OUTPUT`. `--nbval-sanitize-with sanitize.cfg` applies regex substitutions to both the expected and the actual output, which is how you deal with timestamps you cannot remove.

## Knowing when to leave

A notebook stops being the right container roughly when you start scrolling to find a function you wrote earlier, or when you copy a cell between two notebooks. At that point the code wants to be a module: importable, testable with ordinary `pytest`, diffable, and callable from both notebooks.

This is the normal lifecycle. The notebook keeps doing what it is good at, the narrative and the plots, and imports the parts that have settled.

```python
%load_ext autoreload
%autoreload 2

from myproject.analysis import load_samples, summarise
```

`%autoreload 2` re-imports changed modules before each cell runs, so editing `myproject/analysis.py` takes effect without restarting the kernel. Without it, your edits appear to do nothing, which is a confusing few minutes at exactly the moment you have started splitting code out.

!!! tip "Reactive notebooks"

    [marimo](https://marimo.io/) is a notebook format that stores as a plain
    `.py` file and re-runs dependent cells automatically when a value changes.
    Hidden state and unreadable diffs, the two problems this page spends the
    most words on, are both designed out rather than managed. Worth a look for
    a new project, though it is not a drop-in replacement for an existing
    `.ipynb` corpus.

## Sharing

To let someone read a notebook, `jupyter nbconvert --to html analysis.ipynb` produces a standalone file, and GitHub renders committed `.ipynb` files directly. Both need outputs present, which is the tension with stripping them described above. Pairing with Jupytext, or publishing an executed copy separately from the stripped source, resolves it.

To let someone run it, [Binder](https://mybinder.org/) builds an environment from a repository's dependency file and serves a live session. It works only for public repositories, caps memory at around 2 GB, and culls idle sessions, so treat it as a demo path rather than somewhere real analysis happens.

[Google Colab](https://colab.research.google.com/) opens any notebook from GitHub and sometimes offers a free GPU runtime, subject to availability and usage limits. It ignores your environment and provides its own, so Colab notebooks generally need a `pip install` cell at the top and are best treated as a separate distribution of the work.

## Further reading

- [Jupyter documentation](https://docs.jupyter.org/en/latest/)
- [nbdime documentation](https://nbdime.readthedocs.io/)
- [Jupytext documentation](https://jupytext.readthedocs.io/)
- [Papermill documentation](https://papermill.readthedocs.io/)
- [nbstripout](https://github.com/kynan/nbstripout)
- [nbval documentation](https://nbval.readthedocs.io/)
- [nbQA](https://nbqa.readthedocs.io/), for running ruff, black, or mypy over notebooks
- Rule, A. et al. (2019), [Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks](https://doi.org/10.1371/journal.pcbi.1007007), *PLOS Computational Biology*
