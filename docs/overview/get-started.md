# Get Started

There is no required order here, and no page assumes you have read the ones before it. Pick the section that matches what is in your way.

## If you are new to research software engineering

Start with version control, because most of the other practices assume it:

1. [Git and Github for collaboration](../fundamentals/git-github.md) covers forking, branching, pull requests, and reviews.
2. [Commit messages convention](../fundamentals/conventional-commits.md) explains the Conventional Commits format this project and many others use.
3. [Git, Github, and Conventional commit for ultimate collaboration](../tutorials/00-git-commit.md) walks the whole thing end to end as a hands-on tutorial.

If Git itself is new rather than just the collaboration workflow, the Software Carpentry [Version Control with Git](https://swcarpentry.github.io/git-novice/) lesson is the prerequisite, and the tutorial above says so too.

## If your code runs for you and nobody else

This is the most common problem we see, and it is almost always an environment problem. The Computing development environments chapter covers it:

- [Pixi](../fundamentals/computing-development-environments/pixi.md) is what we recommend, for new projects and for migrating existing ones. It ties the environment to the project directory and writes a lock file by default, which conda makes you opt into.
- [Conda/Mamba](../fundamentals/computing-development-environments/conda-mamba.md) if you have inherited an `environment.yml` and need to understand what it does and does not guarantee before moving off it.
- [Docker](../fundamentals/computing-development-environments/docker.md) when the environment includes system libraries, compilers, or services a language package manager cannot install.
- [Notebooks and interactive environments](../fundamentals/computing-development-environments/notebooks-interactive-environments.md) if the thing that will not reproduce is a notebook.

## If something is broken or slow

[Debugging with VS Code](../fundamentals/test-debug.md) is worth reading even if you already know how to set a breakpoint. It covers debugging unit tests and stepping into Jupyter notebooks, then the cases where print statements stop working: pre-launch tasks, and attaching to a process that is already running. It comes with [exercise materials](https://github.com/uw-ssec/rse-guidelines/tree/main/exercises/vscode-debugging) you can run.

For slow rather than broken, [CPU and Memory Profiling](../advanced/profiling.md) covers the Python profiling tools from `%time` up through Scalene and Memray, and the sampling-versus-deterministic tradeoff that decides which one to reach for.

## If you are publishing or handing work off

[Code Sharing and Deployment](../fundamentals/share-deploy.md) covers GitHub Actions and Codespaces for automating the handoff.

For Python libraries specifically, the [Scientific Python Library Development Guide](https://learn.scientific-python.org/development/) is more thorough than anything we would duplicate here, and we point at it deliberately rather than maintaining our own version.

## If you want to use AI tooling well

The [AI for Software Engineering](../fundamentals/ai-for-software-engineering/github-copilot.md) chapter covers [GitHub Copilot](../fundamentals/ai-for-software-engineering/github-copilot.md), [working with ChatGPT](../fundamentals/ai-for-software-engineering/working-with-chatgpt.md), and [running local LLMs](../fundamentals/ai-for-software-engineering/local-llms.md) when your data cannot leave your machine.

## A note on scope

As the [welcome page](../index.md) says, these are quick guides rather than an extensive knowledge base. Where a topic is already covered well by a community that maintains it full time, we link out instead of restating it. The pages we do write are the ones we needed ourselves.

Sections still being written are marked "Coming soon" with a link to their tracking issue. [Contributions are welcome](https://github.com/uw-ssec/rse-guidelines), including telling us that something here is out of date.
