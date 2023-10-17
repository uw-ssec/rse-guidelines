# Code Sharing and Deployment

The process of code sharing and deployment is a critical aspect of modern software development.
Collaborative projects require efficient methods to share, test, and deploy code changes, while ensuring reliability and consistency.
In this tutorial, we explore the use of **Docker**, **GitHub Actions**, and **Github Codespaces** working together to simplify code collaboration, sharing, deployment,
making research and software development reproducible and collaborative.

## Docker: Containerization for Consistency

Docker is a containerization platform that simplifies packaging applications and their dependencies into lightweight, portable containers.
These containers can run consistently across different environments, eliminating the "it works on my machine" problem.

**Key features**:

- **Isolation**: Docker containers encapsulate applications and their dependencies, ensuring that they run consistently and independently of the host environment.
- **Portability**: Docker containers can be easily moved between different environment: development, testing, and production. This guarantees consistent behavior.
- **Version Control**: Docker file and/or images can be versioned, allowing you to maintain and track different versions of your application.
- **Microservices Architecture**: Docker containers are well-suited for microservices-based architectures, enabling you to break down complex applications into smaller, manageable components.

### Containers vs VM

![container-vm](https://www.docker.com/wp-content/uploads/2021/11/docker-containerized-and-vm-transparent-bg.png)

#### Virtual Machine (VM)

Virtual machines (VMs) are an abstraction of physical hardware turning one server into many servers. The hypervisor allows multiple VMs to run on a single machine. Each VM includes a full copy of an operating system, the application, necessary binaries and libraries – taking up tens of GBs. VMs can also be slow to boot.

#### Containers

Containers are an abstraction at the app layer that packages code and dependencies together. Multiple containers can run on the same machine and share the OS kernel with other containers, each running as isolated processes in user space. Containers take up less space than VMs (container images are typically tens of MBs in size), can handle more applications and require fewer VMs and Operating systems.

### Docker Architecture

![docker-architecture](https://docs.docker.com/get-started/images/docker-architecture.png)

The Docker Client and Host (Server) in combination is called the Docker Engine. Docker Engine is an open source containerization technology for building and containerizing your applications. Docker Engine acts as a client-server application with:

- A server with a long-running daemon process `dockerd`.
- APIs which specify interfaces that programs can use to talk to and instruct the Docker daemon.
- A command line interface (CLI) client `docker`.

You can read more details about the Docker Architecture [here](https://docs.docker.com/get-started/overview/#docker-architecture).

We'll cover **Registry** on the core concept below.

### Installation

You can install docker directly from their website at [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).

### Concepts of Docker

#### 1. Docker file

A Docker file is a file containing steps to building your docker image.

Example of an awesome `Dockerfile` can be found [here](https://github.com/pangeo-data/pangeo-docker-images/blob/master/base-image/Dockerfile). What's great about this image is that it sets up conda and jupyter server, which is useful when working on research related work.

With Docker file, you can share this with anyone and that person will get the same exact image as you after it's built.
Also, since it is a file, you can version control it with git.

#### 2. Docker Image

A Docker Image is the "built" version of a Docker file.
This typically live on your internal Docker host or an external Registry, so you can't store a Docker image in git.

An example of a docker image that has been built with the Docker file above can be found [here](https://hub.docker.com/layers/pangeo/base-image/latest/images/sha256-1854ca62ef75f1e017e1920b3a167c62cb5f0ee921f13c3247fc4b016e5be3be?context=explore). That is the published image for with specific file sha, which allows for a specific version of that image, just like your regular files!

#### 3. Docker Container

A container is a standard unit of software that get's spun up from an image.
This is the running software application that you have built.
It is lightweight and easily scalable and tools like [Kubernetes](https://kubernetes.io/) are used to orchestrate the deployment of these containers in production.

#### 4. Container Registry

As you saw and I mentioned above that images can be stored in a Registry.
The most popular free registry currently is [Docker Hub](https://hub.docker.com/),
but there is now the [Github Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) as well.

Similarly like an app store, the Docker Hub serves various images and image versions. As you can see [here](https://hub.docker.com/r/pangeo/base-image/tags) these are the various `tags` for the example image.
Tags are like versions, you can tag images however you like!

**You can go through the [Docker 101](https://www.docker.com/101-tutorial/) lab to practice the concepts above! And the [official docker website](https://docs.docker.com/get-started/) has lots of great "get started" learning resources.**

## GitHub Actions: Automating Your Workflow

GitHub Actions is a versatile and flexible automation tool provided by GitHub.
It allows you to create and customize workflows that automatically respond to events in your code repository.
These workflows can include tasks like building, testing, and deploying code.

**Key features**:

- **Event-Driven Automation**: GitHub Actions is event-driven, which means you can trigger specific actions based on events such as code pushes, pull requests, or issue creation.
- **Customizable Workflows**: You can create custom workflows by defining a series of jobs and steps in a YAML file, allowing you to tailor automation to your project's specific needs.
- **Wide Range of Actions**: GitHub Actions provides a marketplace of pre-built actions that you can use in your workflows, simplifying tasks like deploying to cloud services or running tests.
- **Continuous Integration and Deployment**: You can set up continuous integration (CI) and continuous deployment (CD) pipelines to automate testing and deployment processes.
- **Cross-Platform Compatibility**: GitHub Actions supports various operating systems and programming languages, making it suitable for a wide range of projects.

## Github Codespaces: Collaborative Development Environment

GitHub Codespaces is a powerful development environment that offers a range of features to simplify the development process.

**Key features**:

- **Instant Setup**: Codespaces eliminates the need for developers to set up their development environment locally. You can access a fully configured, cloud-hosted development environment in seconds, saving time and reducing setup hassles.
- **Accessibility**: Access your development environment from anywhere with an internet connection, whether you're on your work computer, personal laptop, tablet, or even smart phones. This accessibility ensures you can code wherever you are.
- **Platform-Agnostic**: Codespaces works consistently across different operating systems, including Windows, macOS, and Linux.
- **Customization**: Customize your Codespace by installing specific extensions, configuring settings, and adding tools that align with your project's requirements. This flexibility allows you to create an environment tailored to your needs.
- **Consistency**: Codespaces ensure a consistent development environment for all team members since it's essentially a Docker container!
- **Integration with GitHub**: Codespaces are fully integrated with GitHub repositories, allowing you to open, work in, and connect your Codespace directly from a project's repository.
- **Version Control**: Codespaces support version control, so you can track changes and collaborate on your code seamlessly with Git, making it an excellent tool for managing code development.
- **Shareability**: You can instantly share your Codespace with others, simplifying collaboration with colleagues or assisting someone in troubleshooting a problem. Sharing is as simple as sending a link.
- **Scalability**: Codespaces make it easy to scale your development environment as needed, adding more resources or configuring the environment to your desire.
