# Kubernetes

## Overview

Kubernetes (often abbreviated as K8s) is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It was originally developed by Google and is now maintained by the Cloud Native Computing Foundation (CNCF).

## Core Concepts

### Pods

Pods are the smallest deployable units in Kubernetes. A Pod represents a single instance of a running process in your cluster and can contain one or more containers that share storage and network resources.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  containers:
  - name: app-container
    image: nginx:latest
    ports:
    - containerPort: 80
```

### Deployments

Deployments provide declarative updates for Pods and ReplicaSets. They allow you to describe the desired state of your application, and the Deployment controller changes the actual state to match the desired state.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: example
  template:
    metadata:
      labels:
        app: example
    spec:
      containers:
      - name: app
        image: example-app:1.0
        ports:
        - containerPort: 8080
```

### Services

Services provide a stable endpoint to access a group of Pods. They enable network access to a set of Pods and provide load balancing across them.

**Service Types:**
- **ClusterIP**: Exposes the service on an internal IP within the cluster (default)
- **NodePort**: Exposes the service on each Node's IP at a static port
- **LoadBalancer**: Exposes the service externally using a cloud provider's load balancer
- **ExternalName**: Maps the service to a DNS name

```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
spec:
  selector:
    app: example
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
```

### ConfigMaps and Secrets

**ConfigMaps** store non-confidential configuration data in key-value pairs, while **Secrets** store sensitive information such as passwords, tokens, or keys.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_url: "postgres://db:5432"
  log_level: "info"
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  password: cGFzc3dvcmQxMjM=  # base64 encoded
```

### Namespaces

Namespaces provide a mechanism for isolating groups of resources within a single cluster. They are useful for dividing cluster resources between multiple users or teams.

### Persistent Volumes (PV) and Persistent Volume Claims (PVC)

Persistent Volumes provide a way to store data that persists beyond the lifecycle of individual Pods. PVCs are requests for storage by users.

## Kubernetes Architecture

Kubernetes follows a master-worker architecture:

**Control Plane Components:**
- **API Server**: The front-end for the Kubernetes control plane
- **etcd**: Consistent and highly-available key-value store for all cluster data
- **Scheduler**: Assigns Pods to Nodes based on resource requirements
- **Controller Manager**: Runs controller processes to regulate the state of the cluster

**Node Components:**
- **kubelet**: Agent that ensures containers are running in Pods
- **kube-proxy**: Maintains network rules for Pod communication
- **Container Runtime**: Software responsible for running containers (e.g., Docker, containerd)

## Packaging with Helm

### What is Helm?

Helm is the package manager for Kubernetes, often described as the "apt/yum/homebrew for Kubernetes." It simplifies the deployment and management of applications on Kubernetes clusters by packaging all the necessary resources into reusable charts.

### Key Concepts

**Helm Charts**: A collection of files that describe a related set of Kubernetes resources. A chart contains:
- `Chart.yaml`: Metadata about the chart (name, version, description)
- `values.yaml`: Default configuration values
- `templates/`: Directory containing Kubernetes manifest templates
- `charts/`: Directory for chart dependencies (optional)

**Releases**: An instance of a chart running in a Kubernetes cluster. Each installation of a chart creates a new release.

**Repositories**: Locations where charts can be stored and shared.

### Basic Helm Chart Structure

```
my-app/
├── Chart.yaml
├── values.yaml
├── charts/
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    ├── configmap.yaml
    └── _helpers.tpl
```

### Example Chart.yaml

```yaml
apiVersion: v2
name: my-app
description: A Helm chart for my application
type: application
version: 0.1.0
appVersion: "1.0"
```

### Example values.yaml

```yaml
replicaCount: 3

image:
  repository: my-app
  tag: "1.0"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: false
  className: ""
  hosts:
    - host: example.local
      paths:
        - path: /
          pathType: Prefix

resources:
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 100m
    memory: 128Mi
```

### Template Example (templates/deployment.yaml)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-app.fullname" . }}
  labels:
    {{- include "my-app.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "my-app.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "my-app.selectorLabels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        imagePullPolicy: {{ .Values.image.pullPolicy }}
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
        resources:
          {{- toYaml .Values.resources | nindent 12 }}
```

### Common Helm Commands

```bash
# Search for charts in repositories
helm search repo <keyword>

# Install a chart
helm install <release-name> <chart-name>

# Install with custom values
helm install <release-name> <chart-name> -f custom-values.yaml

# List all releases
helm list

# Upgrade a release
helm upgrade <release-name> <chart-name>

# Rollback to a previous release
helm rollback <release-name> <revision>

# Uninstall a release
helm uninstall <release-name>

# Create a new chart
helm create <chart-name>

# Validate chart syntax
helm lint <chart-path>

# Package a chart for distribution
helm package <chart-path>
```

### Best Practices for Helm Charts

1. **Use values.yaml for configuration**: Keep all configurable parameters in values.yaml rather than hardcoding them in templates
2. **Include resource limits**: Always specify resource requests and limits for containers
3. **Use helper templates**: Create reusable template functions in `_helpers.tpl` for labels and selectors
4. **Document your values**: Add comments in values.yaml explaining each configuration option
5. **Version your charts**: Follow semantic versioning for both chart version and app version
6. **Test your charts**: Use `helm lint` and `helm template` to validate before installation
7. **Use .helmignore**: Exclude unnecessary files from your chart package
8. **Implement health checks**: Include liveness and readiness probes in your deployments

## Additional Resources

- [Official Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)
- [Helm Documentation](https://helm.sh/docs/)
- [Kubernetes Patterns Book](https://www.redhat.com/en/resources/kubernetes-patterns-ebook)
- [CNCF Landscape](https://landscape.cncf.io/)