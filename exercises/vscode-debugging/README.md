# VS Code debugging exercises

Supporting materials for [Debugging with VS Code](../../docs/fundamentals/test-debug.md).

These files used to live in a separate `uw-ssec/vscode_debugging` repository. That
repo was archived and private, so the tutorial was unusable for anyone outside the
org ([#79](https://github.com/uw-ssec/rse-guidelines/issues/79)). They now live here.

## Setup

Open **this directory** in VS Code — not the repository root. The debug
configurations in `.vscode/` use `${workspaceFolder}`, so they only resolve when
this folder is the workspace root.

```bash
code exercises/vscode-debugging
```

Then create the environment:

```bash
pixi install
```

If you do not have Pixi yet, see the [Pixi page](../../docs/fundamentals/computing-development-environments/pixi.md) for installation.

Select the interpreter in VS Code via the Command Palette
(`Cmd+Shift+P` / `Ctrl+Shift+P`) then **Python: Select Interpreter**. The
`delete_today` task resolves whichever interpreter you pick here, so the
pre-launch exercise will not work until you have.

You will also need the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
and [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
extensions. The latter installs automatically with the former.

## What's here

| File | Used by |
| --- | --- |
| `reverse.py` | Basic debugging — stepping, breakpoints, data inspection |
| `tests.py` | Unit test debugging, via the `PyTest` configuration |
| `notebook.ipynb` | Jupyter notebook debugging |
| `gendate.py` | Pre-launch tasks, via `Python: GenDate` |
| `deleter.py` | Remote debugging, via `Python: Attach using Port` |
| `.vscode/launch.json` | All four debug configurations |
| `.vscode/tasks.json` | The `delete_today` pre-launch task |

## Sanity check

```bash
pixi run demo    # or: python reverse.py
pixi run test    # or: pytest tests.py
```

`pixi run demo` prints three reversals of `hello world`; `pixi run test` passes
two tests.
