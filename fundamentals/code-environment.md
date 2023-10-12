# Computing Environment

In the world of data science, machine learning, and scientific computing, having a flexible and efficient computing environment is essential.
Two tools that have gained immense popularity in recent years for creating such environments are Conda and Jupyter Notebook.
These tools, though distinct in their functions, often work in tandem to provide a robust and versatile ecosystem for developers and researchers.
In this tutorial, we will explore what Conda and Jupyter Notebook are, how they work together, and how they create a collaborative and reproducible computing ecosystem.

## Conda: Your Virtual Environment and Package Manager

[Conda](https://conda.io/en/latest/) is a package management and environment management system that simplifies the process of setting up, managing, and sharing software packages and libraries. It is particularly popular in the Python ecosystem but can be used for multiple programming languages. Conda allows users to create isolated virtual environments, each with its own set of dependencies and packages. This isolation ensures that different projects or tasks do not interfere with each other.

**Key Features**:

- **Package Management**: Conda offers an extensive repository of pre-built packages and libraries. Users can easily install, update, and remove packages using simple commands.
- **Environment Isolation**: Virtual environments created with Conda can have their specific Python versions and libraries. This helps avoid compatibility issues between projects.
- **Cross-Platform Compatibility**: Conda works seamlessly across Windows, macOS, and Linux, making it ideal for cross-platform development and deployment.

### Installation

There are 2 distribution of conda: [Anaconda](https://www.anaconda.com/download) and [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/).
Since conda is able to create separate environments with whatever python packages you want, we recommend installing *Miniconda* since it’s much more lightweight to install.
We think that this is a good distribution to get started on, especially if you are still learning about all the various tools for data science.

Installation instruction for Miniconda can be found [here](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html).

**NOTE: If you already have python installed in your system please read [this](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages) to make sure that you’re using python from conda.**

### Concepts of Conda

<details><summary> 💡 Conda Help and Manual</summary>
<p>

To see the full documentation for any command, type the command followed by --help. For example, to learn about the conda update command:
```
conda update --help
```

</p>
</details>

#### 1. Environments

![conda environments](https://geohackweek.github.io/datasharing/assets/img/conda/conda-env2.jpeg)

What is a conda environment?

- Similar to python virtual environments (venv)
- A set of isolated packages in a directory
- Able to be shared via environment files

```console
# List out available environments
conda env list # The starred * environment is the current activate environment

# Create conda environment from command line (Not Best Practice)
conda create --name myenv --channel conda-forge python=3.10

# Activate conda environment
conda activate myenv

# Deactivate conda environment
conda deactivate

# Create conda environment from environment file (Recommended Best Practice)
conda env create --file environment.yml

# Removing conda environments
conda env remove --yes --name myenv
```

Sample of `environment.yml`

```yaml
name: tutorial-env
channels:
- conda-forge
dependencies:
- python=3.7
- numpy
- matplotlib
- pandas
- bokeh
- rise
- nb_conda_kernels
- ipykernel
```

<details><summary><strong>⭐ Best practice to share environments</strong></summary>
<p>


1. When starting a new environment, always generate it from an environment file rather than the command line.
2. As you add packages to the environment, be sure to update the environment file.
3. Unless you have to (i.e. Production Environments), try to avoid specifying the version of each package. This will ensure you have the most up to date version that will work across platform.

If you follow these guidelines, you should be able to give your environment file to anyone, and they will be able to install your packages with no problem.

**NOTE: In addition to the above practice, you can also use a tool called [`conda-lock`](https://github.com/conda/conda-lock).
This tool allows you to completely capture the exact versions of packages in your environment from an `environment.yml` at that time of locking.
This allows for greater reproducibility across all platforms.**

</p>
</details>

#### 2. Channels

![conda channels](https://geohackweek.github.io/datasharing/assets/img/conda/conda-channels.jpeg)

What is a conda channel?

- Similar to linux repository (or app store)
- The service is hosted for free at Anaconda Cloud

```console
# List out your channels and priorities

conda config --get channels

# If you have a few trusted channels that you prefer to use, you can pre-configure these so that every time you are creating an environment, you won’t need to explicitly declare the channel.

conda config --add channels conda-forge

# strict priority and conda-forge at the top will ensure
# that all of your packages will be from conda-forge unless they only exist on defaults

conda config --set channel_priority strict
conda config --set show_channel_urls True
```

**NOTE: The highest priority channel is where your packages will be installed from no matter if another channel has a higher version!**

<details><summary>⭐ Conda Forge Channel</summary>
<p>

[Conda forge](https://anaconda.org/conda-forge) is a community led collection of recipes, build infrastructure and distributions for the conda package manager.

Watch Filipe’s talk from pycon, one of the conda-forge lead developer, https://www.youtube.com/watch?v=qJFkIuzD6tI for more info about how to put your packages into the conda-forge channel!

</p>
</details>

#### 3. Packages

What is a conda package?

- A compiled software package, but when installed also include all of its dependencies even the lower level ones
- Cross platform
- Made from **recipes**

You can search for conda packages at https://anaconda.org/ or the terminal shown below.

```console
# Look at the packages you have installed
conda list

# Let's search for gdal conda
conda search gdal

# Install a single conda package
conda install -c conda-forge gdal

# Or install multiple packages
conda install -c conda-forge gdal fiona

# Removing a conda package
conda remove -n myenv gdal
```

#### 4. Recipes

Instruction on how to compile the conda package and its metadata

```yaml
package:
  name: pandas
  version: 
source:
  url: https://github.com/pydata/pandas/archive/v.tar.gz
  sha256: d9f67bb17f334ad395e01b2339c3756f3e0d0240cb94c094ef711bbfc5c56c80
build:
  number: 0
  script: python setup.py install --single-version-externally-managed --record=record.txt
about:
  home: http://pandas.pydata.org
  license: BSD 3-clause
  summary: 'High-performance, easy-to-use data structures and data analysis tools.'
extra:
  recipe-maintainers:
    - jreback
    - jorisvandenbossche
    - TomAugspurger
```

**For official walkthrough go to [https://bit.ly/tryconda](https://bit.ly/tryconda)**

**For conda cheat sheet, go to [https://tinyurl.com/y49fjnoj](https://tinyurl.com/y49fjnoj)**

#### 5. Solver

This is not a core concept, but is something to be aware of as you're working with conda.
One of the wonderful feature of conda is the ability to solve version dependencies for all the packages to be installed under the hood.
This requires some algorithm to be executed and as of late, the default `classic` solver for conda can be very slow at performing this solving.
As of [March 16th, 2022](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community), there is now a faster solver for conda called `libmamba`.

You can simply install this solver:

```console
conda install -n base conda-libmamba-solver
```

And then set this solver as default:

```console
conda config --set solver libmamba
```

**For more information and technical details about this, go to [https://conda.github.io/conda-libmamba-solver/libmamba-vs-classic/](https://conda.github.io/conda-libmamba-solver/libmamba-vs-classic/)**

## Jupyter Notebook: A Powerful Interactive Computing Environment

The Jupyter Notebook a.k.a IPython Notebook is **an interactive computing environment** that enables users to author notebook documents that include:

- Live code
- Interactive widgets
- Plots
- Narrative text
- Equations
- Images
- Video

These documents provide a complete and self-contained record of a computation that can be converted to various formats and shared with others using email, online storage systems, version control systems (like git/[GitHub](http://github.com/)) or [nbviewer.org](https://nbviewer.org/g).

**Key Features**:

- **Code Interactivity**: You can run code cells interactively, making it easy to experiment and visualize the results in real-time.
- **Rich Media Support**: Jupyter Notebook supports the inclusion of images, videos, and interactive visualizations to enhance your data presentation.
- **Sharing and Collaboration**: Notebooks can be shared easily with colleagues and collaborators, promoting effective collaboration in data analysis and research.
- **Kernels**: Jupyter supports various kernels, allowing you to work in different programming languages within the same notebook.

### Installation

If you already have a conda environment set up you can simply install a jupyter notebook application:

```console
# Install JupyterLab application
conda install -c conda-forge jupyterlab
```

or you can directly install via `pip`:

```console
# Install JupyterLab application
pip install jupyterlab
```

### Concepts of Jupyter Notebook

#### 1. Notebook Application

The notebook application is usually an in-browser, web application such as [Jupyter Notebook](http://jupyter.org/) or [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/). However, a popular Integrated Development Environment (IDE) like Visual Studio Code (VSCode) now supports [Jupyter Notebook natively](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

The notebook application enables users to:

- **Edit code in the application**, with automatic syntax highlighting, indentation, and tab completion/introspection.
- **Run code directly in the application**, with the results of computations attached to the code which generated them.
- See the results of computations with **rich media representations**, such as HTML, LaTeX, PNG, SVG, PDF, etc.
- Create and use **interactive JavaScript widgets**, which bind interactive user interface controls and visualizations to reactive kernel side computations.
- Author **narrative text** using the [Markdown](https://daringfireball.net/projects/markdown/) markup language.
- Build **hierarchical documents** that are organized into sections with different levels of headings.
- Include mathematical equations using **LaTeX syntax in Markdown**, which are rendered directly by [MathJax](http://www.mathjax.org/).

#### 2. Kernels

Through IPython's kernel and messaging architecture, the Notebook allows code to be run in a range of different programming languages. For each notebook document that a user opens, the web application starts a kernel that runs the code for that notebook. Each kernel is capable of running code in a single programming language and there are kernels available in over [100 programming languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

[IPython](https://github.com/ipython/ipython) is the default kernel, it runs Python code.

Each of these kernels communicate with the notebook web application and web browser using a JSON over ZeroMQ/WebSockets message protocol that is described [here](https://jupyter-client.readthedocs.io/en/latest/messaging.html#messaging). Most users don't need to know about these details, but it helps to understand that "kernels run code."

##### Conda kernels

`nb_conda_kernels` extension for Jupyter Notebook or JupyterLab application allows one conda environment to access kernels for Python, R, and other languages found in other conda environments.

When a kernel from an external environment is selected, the kernel conda environment is automatically activated before the kernel is launched. This allows you to utilize different versions of Python, R, and other languages from a single Jupyter installation.

To install this extension simply run in the same conda environment where you've installed either jupyter notebook or jupyterlab application:

```console
conda install -c conda-forge nb_conda_kernels
```

**NOTE: In order for `nb_conda_kernels` to "see" other conda environment, you need to install `ipykernel` package to that environment**

#### 3. Notebook documents

Notebook documents contain the **inputs and outputs** of an interactive session as well as **narrative text** that accompanies the code but is not meant for execution. **Rich output** generated by running code, including HTML, images, video, and plots, is embedded in the notebook, which makes it a complete and self-contained record of a computation.

When you run the notebook web application on your computer, notebook documents are just **files on your local filesystem with a `.ipynb` extension**. This allows you to use familiar workflows for organizing your notebooks into folders and sharing them with others using email, online storage, and version control systems.

Notebooks consist of a **linear sequence of cells**. There are three basic cell types:

- **Code cells**: Input and output of live code that is run in the kernel
- **Markdown cells**: Narrative text with embedded LaTeX equations
- **Raw cells**: Unformatted text that is included, without modification, when notebooks are converted to different formats using nbconvert

Internally, notebook documents are [JSON](https://en.wikipedia.org/wiki/JSON) data with binary values [base64](http://en.wikipedia.org/wiki/Base64) encoded.
This allows them to be **read and manipulated programmatically** by any programming language.
Because JSON is a text format, notebook documents are version control friendly.

**Notebooks can be exported** to different static formats including HTML, reStructeredText, LaTeX, PDF, and slide shows using Jupyter's nbconvert utility.

Furthermore, any notebook document available from **a public URL on or GitHub can be shared** via [https://nbviewer.org](https://nbviewer.org).
This service loads the notebook document from the URL and renders it as a static web page.
The resulting web page may thus be shared with others **without their needing to install Jupyter**.

##### Jupyter Book

A collection of Jupyter Notebooks can be compiled together and published on a static website using [Jupyter Book](https://jupyterbook.org/en/stable/intro.html).
This allows for easy access to the contents of your jupyter notebooks including code and figures.
In fact, this whole tutorial and website is created with Jupyter Book!

## The Synergy Between Conda and Jupyter Notebook

While Conda and Jupyter Notebook serve different primary purposes, as you have seen, they complement each other exceptionally well.
Here's how they work together to create a powerful computing environment:

- **Virtual Environments**: Conda allows you to create isolated virtual environments for different projects. You can install Jupyter Notebook within a Conda environment to ensure that your notebooks have access to the specific libraries and packages required for a given task.

- **Dependency Management**: Conda simplifies package and library management, ensuring that the required dependencies are available for your Jupyter Notebook projects. You can install packages in your Conda environment, and Jupyter Notebook can access them without conflicts.

- **Reproducibility**: By creating Conda environments for your Jupyter Notebook projects, you achieve a high level of reproducibility. You can easily share the environment configuration, making it possible for others to recreate your working environment effortlessly.

- **Portability**: With Conda, you can export and share your environment configuration as a YAML file. This can be particularly handy when working with colleagues or moving your projects to different machines or cloud servers.

## Exercise: Create a jupyter notebook and conda environment file

For this exercise, we will:

- create a simple conda environment
- download an existing jupyter notebook
- run the jupyter notebook

### Conda environment

Open your favorite text editor and copy and paste below, and save to a file called `environment.yml`

```yaml
name: myenv
channels:
- conda-forge
dependencies:
- python=3.10
- numpy
- jupyterlab
```

Create the conda environment:

```console
conda env create -f environment.yml
```

### Jupyter notebook

We will now create a new Jupyter Notebook by doing the following.
Our new Jupyter Notebook will require [`numpy`](https://numpy.org/) package. This package should have been installed in the `myenv` conda environment created above.

To spin up the Notebook application to edit/run the notebook, we will use JupyterLab, which also have been installed.

First, activate your conda environment

```console
conda activate myenv
```

Run JupyterLab server on the background to spin up in the browser.
Once it's spun up, you can hide the terminal and start working in the browser:

```console
jupyter lab
```

In the jupyter lab application within the browser, do the following:

1. In the first cell of the notebook, put a heading and short description of our work in markdown format.

    ```markdown
    # My first notebook

    This is my first notebook example.
    I will be running some code later.
    ```

    Ensure that the cell type is `Markdown` by going to the cell type dropdown button in the toolbar and selecting "Markdown", so it can render properly.

    ![nb-cell-type](../assets/images/nb-cell-type.png)

2. On the next cell, import numpy and print it's version:

    ```python
    import numpy

    print(numpy.__version__)
    ```

3. On the last cell for this simple example, we'll create an array of integer from 0 to 9 and print it:

    ```python
    array = numpy.arange(10)

    print(array)
    ```

4. When you're ready to save the notebook simply do `cmd + S` for MacOS or `ctrl + S` for Windows or Linux, and name the notebook `my-first-notebook.ipynb`.

5. To stop the running server, go back to the terminal and press the following keys on your keyboard: `ctrl+c`.

## Acknowledgements

Conda:

The content for the conda tutorial was imported from [Don Setiawan](https://github.com/lsetiawan), [Conda Introduction](https://nbviewer.org/github/geohackweek/datasharing/blob/master/notebooks/03-Conda.ipynb) with a few tweaks.

Jupyter Notebook:

The content for the jupyter notebook tutorial was imported from [Fernando Perez](https://github.com/fperez), [A quick and practical Intro to Jupyter Notebook](https://github.com/ICESAT-2HackWeek/intro-jupyter-git/blob/master/01-Intro%20Jupyter%20Notebook.ipynb) with a few tweaks.
