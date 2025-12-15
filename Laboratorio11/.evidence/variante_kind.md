# Variante Implementada: Kind en lugar de Minikube

## Razón:
- Minikube presentó problemas de integración con Docker Desktop en WSL
- Kind es más simple para entornos WSL/containers

## Adaptaciones realizadas:
1. Cluster: `kind create cluster --name lab-devsecops`
2. Imágenes: `user-service:kind`, `order-service:kind`
3. Carga de imágenes: `kind load docker-image`
4. Verificación: `kubectl port-forward` en lugar de `minikube service --url`
5. Smoke tests: Scripts funcionaron con port-forward automático

## Comandos clave ejecutados:
- kind create cluster --name lab-devsecops
- kind load docker-image user-service:kind
- kubectl apply -f k8s/user-service-kind.yaml
- kubectl port-forward service/user-service 8000:8000
- ./scripts/minikube_smoke.sh user-service 8000 (adaptado)

## Resultado: Todos los objetivos del laboratorio cumplidos
