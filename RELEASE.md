# Release 2025.11.10 - First Official Release

**Release Date:** November 10, 2025

**Documentation:** [https://rse-guidelines.readthedocs.io/](https://rse-guidelines.readthedocs.io/)

**Repository:** [https://github.com/uw-ssec/rse-guidelines](https://github.com/uw-ssec/rse-guidelines)

---

## Project History

The UW SSEC Research Software Engineering Guidelines project was initiated in **August 2023** to codify and share best practices for research software development within the University of Washington Scientific Software Engineering Center (SSEC) and the broader research community.

**Timeline:**
- **August 2023** - Project inception with conventional commits and Python guides
- **October 2023** - Jupyter Book infrastructure, foundational materials (Git, GitHub, environments, debugging by Carlos Garcia Jurado Suarez, Docker)
- **Early 2024** - Tutorial sections and Git workflows
- **Mid 2024** - Conventional commit templates and documentation improvements
- **Fall 2024** - Advanced topics expansion, Flutter/app development, SSEC leadership context
- **October-November 2024** - MkDocs migration, Pixi integration, AI tools chapter, comprehensive README
- **November 2025** - First official release with version 2025.11.10

---

## Overview

This is the **first official release** of the UW SSEC Research Software Engineering Guidelines, representing over two years of collaborative development and refinement. Since its inception in August 2023, the project has grown from initial documentation on conventional commits and Python guides into a comprehensive resource for research software engineering best practices.

This release brings together foundational content with recent enhancements, providing a complete learning path for researchers and software engineers looking to adopt modern development practices.

Key highlights include:

- Comprehensive foundational content covering Git, GitHub, Python environments, debugging, testing, and Docker
- New AI tools for software engineering chapter with practical guidance
- Extensive Pixi package manager tutorial and migration guide
- Complete MkDocs documentation infrastructure with versioning support
- Enhanced README with better navigation and resource organization
- Formal citation support via CITATION.cff file
- Dedicated app development section covering modern frontend frameworks

---

## Foundational Content

Since the project's inception in August 2023, the guidelines have included comprehensive foundational materials that remain core to the documentation:

### Fundamentals Section

- **[Conventional Commits](docs/fundamentals/conventional-commits.md)** - Standardized commit message format for clear version history and automated tooling
- **[Git and GitHub Workflows](docs/fundamentals/git-github.md)** - Version control best practices, branching strategies, and collaboration workflows
- **[Development Environments](docs/fundamentals/code-environment.md)** - Setting up Python environments with conda/mamba, virtual environments, and IDE configuration
- **[Testing and Debugging](docs/fundamentals/test-debug.md)** - Comprehensive guide to debugging in VS Code, including breakpoints, watch expressions, and Jupyter notebook debugging. Originally contributed by Carlos Garcia Jurado Suarez with detailed screenshots and practical examples.
- **[Code Sharing and Deployment](docs/fundamentals/code-sharing.md)** - Best practices for packaging, distribution, and deployment

### Advanced Topics

- **[Docker and Containerization](docs/advanced-topics/docker/)** - Container-based development and deployment, including Docker concepts, best practices, and practical examples
- **[Python Packaging with Grayskull](docs/advanced-topics/packaging/)** - Automated conda recipe generation for Python packages
- **[Performance Profiling](docs/advanced-topics/profiling/)** - CPU and memory profiling techniques for optimizing research software

These foundational materials established the framework that continues to guide the project's growth and development.

---

## New Features and Recent Enhancements

### AI for Software Engineering Chapter

A complete new chapter covering AI-powered development tools has been added to the fundamentals section, providing practical guidance for integrating AI assistants into your workflow:

- **[GitHub Copilot Guide](docs/fundamentals/ai-for-software-engineering/github-copilot.md)** - Comprehensive setup guide including VS Code integration, custom instructions, chat features, and agent mode for autonomous coding tasks
- **[Working with ChatGPT](docs/fundamentals/ai-for-software-engineering/working-with-chatgpt.md)** - Best practices for using large language models for coding assistance, including prompt engineering techniques and effective context management
- **[Local LLMs](docs/fundamentals/ai-for-software-engineering/local-llms.md)** - Running language models locally using Ollama and Continue extension for privacy-conscious development and offline use

This addition reflects the rapidly evolving landscape of software development and provides researchers with practical guidance on leveraging AI tools responsibly and effectively.

### Pixi Package Manager Tutorial

An extensive tutorial on Pixi, the modern evolution of conda package management:

- **Migration guide from conda/mamba** - Side-by-side comparisons and practical migration strategies
- **Project-centric workflow** - Understanding the shift from global environments to project-based dependency management
- **Lockfile-based reproducibility** - Automatic dependency locking for perfect reproducibility across teams
- **Multi-environment support** - Advanced patterns for managing development, testing, and production environments
- **Task management** - Cross-platform task runner with parameter support and dependency chains
- **Platform-specific dependencies** - Handling different requirements across Linux, macOS, and Windows
- **Hands-on exercises** - Two practical exercises covering basic project setup and multi-environment configurations

This comprehensive guide helps teams transition from traditional conda workflows to the more modern, efficient Pixi approach.

### MkDocs Documentation Infrastructure

Complete migration to MkDocs with Material theme, providing a modern, professional documentation experience:

- **Responsive Material theme** - Clean, accessible design with dark mode support
- **Version management with Mike** - Multi-version documentation support for tracking changes across releases
- **Enhanced navigation** - Tabbed navigation, integrated table of contents, and improved search functionality
- **Better content organization** - Restructured documentation hierarchy with clear part/chapter divisions
- **ReadTheDocs integration** - Automated builds and deployment via ReadTheDocs platform
- **LLMs.txt plugin** - Machine-readable documentation for AI-powered tools and agents

### App Development Section

New dedicated section on modern application development:

- **[Flutter Guide](docs/app-development/frontend/flutter.md)** - Cross-platform mobile and web application development with Flutter framework
- Separated from advanced topics into its own top-level section for better discoverability
- Foundation for future expansion into other app development frameworks and patterns

### Citation File (CITATION.cff)

A formal citation file following the Citation File Format standard:

- **Proper academic attribution** - Standardized format for citing these guidelines in research publications
- **Author metadata** - Comprehensive list of contributors with ORCID identifiers where available
- **Version tracking** - Aligned with semantic versioning for clear reference to specific releases
- **License information** - BSD-3-Clause license clearly specified
- **Keywords and abstract** - Comprehensive metadata for discoverability in academic contexts

This addition makes it easy for researchers to properly cite these guidelines in their work and helps track the impact of these resources in the research community.

---

## Documentation Improvements

### Enhanced README

The README has been significantly expanded to provide better onboarding and navigation:

- **Comprehensive overview** - Detailed explanation of the documentation structure and purpose
- **About UW SSEC section** - Information about the team, leadership, and mission
- **Clear documentation structure** - Organized sections covering Fundamentals, Advanced Topics, App Development, Python Resources, and Tutorials
- **Getting Started guides** - Multiple entry points based on user needs (collaboration, environment setup, AI tools, performance)
- **Navigation tips** - Guidance on how to effectively use the documentation
- **Building instructions** - Clear steps for local development using Pixi or pip
- **Contributing guidelines** - Clear process for community contributions following documented best practices

### URL and Link Fixes

- Fixed broken git commit template URL that was causing 404 errors
- Updated all internal documentation links to reflect new MkDocs structure
- Verified external resource links are current and accessible

### Code Formatting Improvements

- Fixed indentation issues in Pixi documentation for better readability
- Improved code block formatting throughout all markdown files
- Applied consistent styling for better rendering in MkDocs

### Content Organization

- Created `_archive` directory for deprecated content while maintaining history
- Removed outdated information from main documentation views
- Consolidated overlapping content between multiple sections
- Updated conda/mamba tutorial to complement new Pixi guide

---

## Infrastructure and Tooling

### Pixi Build System

The repository itself now uses Pixi for development and deployment:

- **`pixi.toml` configuration** - Project dependencies managed via Pixi manifest
- **Cross-platform support** - Supports macOS (ARM64), Linux (x86_64), and Windows (x86_64)
- **Task automation** - Built-in tasks for common operations:
  - `pixi run start` - Serve documentation locally
  - `pixi run rtd-publish` - Build for ReadTheDocs deployment
  - `pixi run release` - Create GitHub releases with proper tagging
- **Lockfile commitment** - `pixi.lock` ensures reproducible builds across all environments
- **GitHub CLI integration** - Automated release creation using `gh` tool

### Documentation Build Dependencies

Updated dependencies for modern documentation tooling:

- **Python 3.11** - Modern Python version for optimal performance
- **MkDocs Material 9.6.16+** - Latest Material theme features
- **MkDocs Jupyter** - Native Jupyter notebook rendering support
- **MkDocs LLMs.txt** - Machine-readable documentation generation
- **Mike 2.1.3+** - Documentation versioning
- **mkdocs-awesome-nav** - Enhanced navigation generation

### Repository Configuration

- Updated `.readthedocs.yml` configuration for Pixi-based builds
- Improved `.gitignore` and `.gitattributes` for better repository hygiene
- Updated CODEOWNERS file to reflect current team structure
- Added sitemap configuration for better SEO and discoverability

---

## Breaking Changes

None. This release is fully backward compatible with previous versions. All existing documentation URLs and structures have been preserved through redirects where necessary.

---

## Contributors

This release was made possible by contributions from the UW SSEC team and community over the past two years:

### Core Contributors

- **Don Setiawan** ([@lsetiawan](https://github.com/lsetiawan)) - Project founder and lead, infrastructure architecture, Pixi integration, documentation organization, MkDocs migration, citation support, foundational content across Git, GitHub, Python environments, Docker, and deployment
- **Carlos Garcia Jurado Suarez** ([@carlosgjs](https://github.com/carlosgjs)) - VS Code debugging documentation with comprehensive visual guides and practical examples
- **Niki Burggraf** ([@nikiburggraf](https://github.com/nikiburggraf)) - App development chapter, advanced topics organization, documentation restructuring, conventional commit template
- **Vraj Rajpura** ([@Vraj1234](https://github.com/Vraj1234)) - AI for Software Engineering chapter, GitHub Copilot guide, local LLMs documentation
- **Ying-Hsiang (YH) Huang** ([@hinxcode](https://github.com/hinxcode)) - Flutter documentation, Docker sections and comprehensive container tutorials
- **Ayush Nag** ([@ayushnag](https://github.com/ayushnag)) - CPU and memory profiling documentation for performance optimization
- **Cordero Core** ([@cdcore09](https://github.com/cdcore09)) - Code review, merge management, and quality assurance
- **David Beck** ([@dacb](https://github.com/dacb)) - Leadership and strategic direction for UW SSEC, organizational context

---

## Upgrade Instructions

If you're building the documentation locally, update your environment:

### Using Pixi (Recommended)

```bash
# Clone or pull the latest changes
git pull origin main

# Update Pixi dependencies
pixi install

# Serve the documentation
pixi run start
```

### Using pip

```bash
# Update dependencies
pip install -r requirements.txt

# Serve the documentation
mkdocs serve
```

---

## Known Issues

None at this time. Please report any issues at [https://github.com/uw-ssec/rse-guidelines/issues](https://github.com/uw-ssec/rse-guidelines/issues).

---

## Looking Ahead

Future releases will focus on:

- Expanding the AI tools section with more practical examples and case studies
- Additional tutorials for common research software engineering workflows
- More advanced deployment patterns (Kubernetes, cloud-native architectures)
- Python packaging best practices aligned with Scientific Python guidelines
- Testing strategies for scientific software
- Performance optimization techniques specific to research computing

---

## Citation

If you use these guidelines in your work, please cite them as:

```bibtex
@software{rse_guidelines_2025,
  author = {Setiawan, Don and Burggraf, Niki and Huang, Ying-Hsiang and Core, Cordero and Garcia Jurado Suarez, Carlos and Rajpura, Vraj and Nag, Ayush},
  title = {Research Software Engineering Guidelines},
  version = {2025.11.10},
  date = {2025-11-10},
  url = {https://github.com/uw-ssec/rse-guidelines},
  doi = {10.5281/zenodo.XXXXXXX}
}
```

Or use the `CITATION.cff` file in the repository for automated citation generation.

---

## Resources

- **Documentation:** [https://rse-guidelines.readthedocs.io/](https://rse-guidelines.readthedocs.io/)
- **Repository:** [https://github.com/uw-ssec/rse-guidelines](https://github.com/uw-ssec/rse-guidelines)
- **Issues:** [https://github.com/uw-ssec/rse-guidelines/issues](https://github.com/uw-ssec/rse-guidelines/issues)
- **UW SSEC:** [https://escience.washington.edu/software-engineering/ssec/](https://escience.washington.edu/software-engineering/ssec/)
- **eScience Institute:** [https://escience.washington.edu/](https://escience.washington.edu/)

---

**Thank you for using the UW SSEC Research Software Engineering Guidelines!**
