# Docker Advanced

## Docker Swarm

> **Note**
> There are some similar tools that you might find confusing when it comes to Docker Swarm:
> 1. [**Swarm mode**](https://docs.docker.com/engine/swarm/)
> * **This is what we are referring to**
> 2. [SwarmKit](https://github.com/moby/swarmkit)
> * This project contains the underlying libraries used by Swarm mode
> 3. [Classic Swarm](https://github.com/docker-archive/classicswarm)
> * Docker's original orchestration tool. Classic Swarm is no longer actively developed, and you should focus on Swarm mode instead

In this guide, we will focus on **Swarm mode** and its related technologies.

Swarm mode is a built-in tool for managing a cluster, which is particularly useful for those of us looking to distribute and scale machine learning workloads across multiple machines with ease.

Additionally, Swarm mode offers [a set of features](https://docs.docker.com/engine/swarm/#feature-highlights). These features make Swarm a powerful tool for managing containerized applications. By leveraging Swarm, users benefit from improved scalability, enhanced security, streamlined deployment processes, etc.

![Swarm Diagram](https://docs.docker.com/engine/swarm/images/swarm-diagram.webp)

#### Core Concepts
1. **Swarm**: A cluster of one or more Docker Engines. A swarm consists of one or more nodes: physical or virtual machines running Docker Engine.
2. **Node**: A Docker Engine participating in the swarm (manager or worker).
3. **Service**: The definition of tasks to execute on nodes.
4. **Task**: A Docker container running on a node, representing the atomic unit of scheduling.

#### Task Lifecycle

Tasks in a swarm go through various states, including `NEW`, `PENDING`, `RUNNING`, and `COMPLETE`. Understanding these states can help in monitoring and troubleshooting ML jobs.

For more details on task states, please visit: [Swarm task states](https://docs.docker.com/engine/swarm/how-swarm-mode-works/swarm-task-states/).

#### Getting Started

To start using Docker Swarm mode:

1. Initialize a swarm (cluster) of Docker Engines
2. Add worker nodes to the swarm
3. Deploy services to the swarm
4. Scale services as needed

For specific commands and a detailed tutorial, please refer to: [Swarm mode official tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/).