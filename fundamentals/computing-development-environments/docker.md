# Docker

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