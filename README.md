# rse-guidelines

[![DOI](https://zenodo.org/badge/678898974.svg)](https://zenodo.org/badge/latestdoi/678898974)

Research Software Engineering Guidelines Documents

## Overview

Welcome to the University of Washington Scientific Software Engineering Center (UW SSEC) Research Software Engineering (RSE) Guidelines repository. This comprehensive collection of tutorials, guides, and best practices is designed to help researchers, software engineers, and developers adopt modern software engineering practices for scientific computing and research projects.

These guidelines are not meant to be an exhaustive knowledge base, but rather a curated set of quick guides and practical tutorials to jumpstart your RSE journey, whether you're just getting started or looking to level up your skills.

## About UW SSEC

The [UW Scientific Software Engineering Center (SSEC)](https://escience.washington.edu/software-engineering/ssec/) at the eScience Institute leverages local software engineering talent to advance scientific frontiers. SSEC is a diverse team of software engineers who work with UW scientists on impactful research projects, infusing them with software industry best practices and delivering open source, reusable software that accelerates research in areas like climate, health, energy, and basic science.

Led by Director [David Beck](https://escience.washington.edu/member/david-beck/) and Head of Engineering [Vani Mandava](https://escience.washington.edu/member/vani-mandava/), SSEC is structured around applied machine learning for science, cloud computing and data management, and community building around scientific software.

## Documentation Website

The full documentation is available at: [https://rse-guidelines.readthedocs.io/](https://rse-guidelines.readthedocs.io/)

## Documentation Structure

The documentation is organized into the following main sections:

### Fundamentals

Core concepts and tools that every research software engineer should know:

- **[Git and GitHub for Collaboration](docs/fundamentals/git-github.md)** - Version control, collaborative workflows, pull requests, and the fork-and-pull model for open source development
- **[Conventional Commits](docs/fundamentals/conventional-commits.md)** - Structured commit message conventions for clear, machine-readable git history
- **[Testing and Debugging](docs/fundamentals/test-debug.md)** - Debugging techniques with VS Code, unit testing, and Jupyter notebook debugging
- **[Code Sharing and Deployment](docs/fundamentals/share-deploy.md)** - GitHub Actions for CI/CD, GitHub Codespaces for collaborative development environments
- **Computing & Development Environments:**
  - [Docker](docs/fundamentals/computing-development-environments/docker.md) - Containerization basics
  - [Conda/Mamba](docs/fundamentals/computing-development-environments/conda-mamba.md) - Python environment management
  - [Pixi](docs/fundamentals/computing-development-environments/pixi.md) - Modern, fast, project-centric package manager (evolution of conda)
  - [Notebooks & Interactive Environments](docs/fundamentals/computing-development-environments/notebooks-interactive-environments.md) - Jupyter and interactive computing
- **AI for Software Engineering:**
  - [GitHub Copilot](docs/fundamentals/ai-for-software-engineering/github-copilot.md) - AI-powered coding assistant setup and best practices
  - [Working with ChatGPT](docs/fundamentals/ai-for-software-engineering/working-with-chatgpt.md) - Using large language models for coding tasks
  - [Local LLMs](docs/fundamentals/ai-for-software-engineering/local-llms.md) - Running language models locally for privacy and offline use

### Advanced Topics

More specialized topics for experienced developers:

- **[Profiling](docs/advanced/profiling.md)** - CPU and memory profiling tools for Python (cProfile, Scalene, Memray, and more)
- **Deployment Strategies & Tools:**
  - [Docker Advanced](docs/advanced/deployment-strategies-tools/docker-advanced.md) - Advanced containerization techniques
  - [Kubernetes](docs/advanced/deployment-strategies-tools/kubernetes.md) - Container orchestration
  - [Cloud Infrastructure and Services](docs/advanced/deployment-strategies-tools/cloud-infrastructure-and-services.md) - Cloud deployment strategies

### App Development

Modern application development technologies:

- **Frontend:**
  - [Flutter](docs/app-development/frontend/flutter.md) - Cross-platform mobile and web application development

### Python-Specific Resources

- **[Python Guidelines](docs/python/README.md)** - Python-specific best practices and links to the [Scientific Python Library Development Guide](https://learn.scientific-python.org/development/)

### Tutorials

Step-by-step hands-on tutorials:

- **[Git, GitHub, and Conventional Commits Tutorial](docs/tutorials/00-git-commit.md)** - Comprehensive tutorial combining Git workflows, forking, pull requests, and conventional commits for effective collaboration

## Getting Started

1. **New to Research Software Engineering?** Start with the [documentation home page](docs/index.md) and explore the fundamentals section
2. **Need to collaborate on code?** Check out the [Git and GitHub guide](docs/fundamentals/git-github.md)
3. **Setting up a development environment?** Learn about [Pixi](docs/fundamentals/computing-development-environments/pixi.md) for modern Python environment management
4. **Want to use AI tools?** See our [GitHub Copilot guide](docs/fundamentals/ai-for-software-engineering/github-copilot.md)
5. **Performance issues?** Dive into [Profiling](docs/advanced/profiling.md) to identify bottlenecks

## Navigation Tips

- Browse the organized documentation on our [ReadTheDocs site](https://rse-guidelines.readthedocs.io/)
- Use the navigation sidebar to explore topics by category
- Each guide includes practical examples, code snippets, and external resources
- Tutorials provide hands-on exercises to practice new skills

## Contributing

We welcome contributions! If you'd like to improve these guidelines or add new content:

1. Fork this repository
2. Create a feature branch following the guidelines in our [Git and GitHub documentation](docs/fundamentals/git-github.md)
3. Follow [conventional commits](docs/fundamentals/conventional-commits.md) for your commit messages
4. Submit a pull request

## Building the Documentation Locally

The documentation is built using [MkDocs](https://www.mkdocs.org/) with the Material theme. To build locally:

```bash
# Install dependencies using pixi (recommended)
pixi install

# Serve the documentation locally
pixi run mkdocs serve

# Or using pip
pip install mkdocs mkdocs-material mkdocs-jupyter awesome-pages mkdocs-llms-txt-plugin mike
mkdocs serve
```

The documentation will be available at `http://127.0.0.1:8000/`.

## License

This documentation is provided under an open source license. Please refer to individual files for specific license information.

## Contact

For questions or suggestions, please [open an issue](https://github.com/uw-ssec/rse-guidelines/issues) or contact the UW SSEC team through the [eScience Institute](https://escience.washington.edu/software-engineering/ssec/).

---

**Happy coding, and welcome to modern research software engineering!**
