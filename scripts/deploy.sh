#!/bin/bash

IMAGE=$1

echo "Deploying image: $IMAGE"

kubectl set image deployment/ci-cd-app app=$IMAGE
kubectl rollout status deployment/ci-cd-app