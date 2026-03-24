# 🚀 CI/CD Pipeline with GitHub Actions, Docker & AWS EKS

## 📌 Overview

This project demonstrates a **production-like CI/CD pipeline** that automates application build, containerization, and deployment to a Kubernetes cluster running on AWS EKS.

It showcases how to eliminate manual deployments and ensure **reliable, repeatable, and scalable delivery**.

---

## 🧩 Client Scenario

A startup was facing:

* Manual deployments
* Frequent production errors
* Lack of deployment consistency

### ✅ Solution

A fully automated CI/CD pipeline that:

* Builds Docker images
* Pushes them to a container registry
* Deploys automatically to Kubernetes (AWS EKS)
* Performs zero-downtime rolling updates

---

## 🏗️ Architecture

GitHub Actions → Docker → AWS EKS → LoadBalancer (ELB)

---

## ⚙️ Tech Stack

* Python (Flask)
* Docker
* GitHub Actions
* Kubernetes (AWS EKS)
* Terraform (Infrastructure as Code)
* AWS (EKS, VPC, Load Balancer)

---

## 🔄 CI/CD Pipeline Flow

1. Code is pushed to GitHub
2. GitHub Actions pipeline is triggered
3. Docker image is built
4. Image is pushed to Docker Hub
5. Deployment is updated in Kubernetes
6. Rolling update is executed (zero downtime)

---

## 🚀 Key Features

* Infrastructure provisioned using Terraform
* Automated CI/CD pipeline
* Kubernetes deployment on AWS EKS
* LoadBalancer exposure via AWS ELB
* Zero-downtime deployments
* Scalable architecture

---

## 🧪 How to Run Locally

```bash
# Build image
docker build -t ci-cd-app -f docker/Dockerfile .

# Run container
docker run -p 5000:5000 ci-cd-app
```

---

## ☸️ Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

---

## 🌐 Access Application

After deployment in EKS:

```bash
kubectl get svc
```

Use the EXTERNAL-IP provided by AWS LoadBalancer.

---

## 📊 Results

* ✅ Automated deployments
* ✅ Reduced manual errors
* ✅ Scalable infrastructure
* ✅ Production-like environment
* ✅ Faster delivery cycles

---

## 💡 What I Learned

* End-to-end CI/CD implementation
* Kubernetes deployment strategies
* AWS EKS provisioning with Terraform
* Debugging real-world infrastructure issues
* Automating deployments with GitHub Actions

---

## 📬 Contact

If you need help implementing CI/CD pipelines, Kubernetes deployments, or cloud infrastructure, feel free to reach out.
