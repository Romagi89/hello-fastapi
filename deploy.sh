#!/bin/bash
set -e

echo "🚀 Deploying FastAPI + PostgreSQL stack to EKS (namespace: harness-eks-demo)"

kubectl create namespace harness-eks-demo --dry-run=client -o yaml | kubectl apply -f -

echo "Applying Kubernetes manifests..."
kubectl apply -f k8s/postgres-secret.yaml
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/postgres-service.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

echo "✅ Deployment completed successfully."
