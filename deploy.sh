#!/usr/bin/env bash

set -e

PROJECT_NAME=$(basename "$PWD" | tr '[:upper:]' '[:lower:]' | tr -d ' .' | tr '_' '-')

DATA_IMAGE="${PROJECT_NAME}-data-service:latest"
AI_IMAGE="${PROJECT_NAME}-ai-service:latest"

echo "---------------------------------"
echo "Projekt: $PROJECT_NAME"
echo "Data Image: $DATA_IMAGE"
echo "AI Image: $AI_IMAGE"
echo "---------------------------------"

echo "Baue Docker Images..."
docker compose up --build -d 

echo "Passe Kubernetes Image-Namen an..."
sed -i.bak "s|image: .*data-service.*|image: ${DATA_IMAGE}|g" k8s/data-service-deployment.yaml
sed -i.bak "s|image: .*ai-service.*|image: ${AI_IMAGE}|g" k8s/ai-service-deployment.yaml

rm -f k8s/*.bak

echo "Wende Kubernetes Konfiguration an..."
kubectl apply -f k8s/

echo "Starte Deployments neu..."
kubectl rollout restart deployment data-service
kubectl rollout restart deployment ai-service

echo "Aktuelle Pods:"
kubectl get pods

echo "Deployment abgeschlossen."