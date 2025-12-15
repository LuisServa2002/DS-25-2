# Laboratorio 11 : DevSecOps total: Docker -> Cadena de suministro -> CI -> Kubernetes (local primero, reproducible)

Luis Andre Trujillo Serva (20220428D)

## Paso 01 : Prerrequisitos
Instalamos todas las herramientas.

## Paso 02 : Preparación de entorno 
La evidencia de este paso se encuentra en `.evidence/env.txt` y `.evidence/make_env.txt`.

## Paso 03 : Desarrollo local (DEV) - pruebas con Docker Compose

### 3.1 User Service

Debido a algunas limitaciones con el almacenamiento edite lo siguiente `MINIKUBE_CPUS` y `MINIKUBE_MEMORY`.

```bash
# Versión/recursos del cluster (puedes overridear con: make K8S_VERSION=v1.33.1 ...)
# K8S_VERSION ?= v1.32.2
MINIKUBE_CPUS ?= 2
MINIKUBE_MEMORY ?= 3072
```
Además realizamos unas modificaciones en `docker/Dockerfile.python-template` ya que no referenciaba al `server.py`.

### 3.2 Order service

He utilizado ambos comando bajo la versión **V1**.

```bash
docker-compose -f docker-compose.order.test.yml up --build --abort-on-container-exit --exit-code-from sut
docker-compose -f docker-compose.order.test.yml down -v
```

## Paso 04 : Supply Chain (SEC) - SBOM + SCA (SARIF + gate) + Firma

### 4.1 Generar SBOM

He seguido los pasos manuales ya que hubo problemas con el Makefile , llegando a generar el artefacto.

```bash
# Construir imagen
docker build -t user-service:sbom-test -f docker/Dockerfile.python-template .

# Guardar como .tar
mkdir -p artifacts
docker save user-service:sbom-test -o artifacts/user-service.tar

# Generar SBOM
syft scan docker-archive:artifacts/user-service.tar -o json > artifacts/user-service-sbom.json
```
La evidencia de este paso se almacena en `artifacts/user-service-sbom.json`.

### 4.2 SCA con gate (Grype -> SARIF)

Nuevamente tenemos problemas con el Makefile , por lo tanto seguiremos comandos manuales (El mismo de **Manual con Grype**). 

La evidencia de este paso se guarda en `artifacts/user-service-grype.sarif`.

### 4.3 Firma y verificación (Cosign)

El comando `cosign sign` requiere que la imagen a firmar esté publicada en un registro de contenedores remoto y accesible (como Docker Hub o GHCR). La imagen `user-service:sbom-test` existe únicamente en el entorno local de Docker, por lo que la herramienta no puede proceder con la firma. El error específico es:
"UNAUTHORIZED: authentication required" al intentar acceder a `index.docker.io/v2/library/user-service/`.

1. **Firma estándar**: `cosign sign --yes user-service:sbom-test`
**FALLÓ**. 

Motivo: Intento de acceso a registro público no autorizado.

2. **Modo experimental local**: `COSIGN_EXPERIMENTAL=1 cosign sign --yes user-service:sbom-test` **FALLÓ**. 

Motivo: La versión de Cosign disponible en el sistema aún intenta contactar el registro remoto.

Revisar la imagen `.evidence/paso4.3(firma).png`

### 4.4 Evidencias de supply chain

Revisar la imagen `.evidence/paso4.4(evidencias).png`
## Paso 05 : CI local con registro (push + firma)

Para lograr configurar debo poner el token generado por GitHub , además de `export IMAGE_REGISTRY=ghcr.io/luisserva2002`. La evidencia se encuentra en `.evidence/logs`.

## Paso 06 : Despliegue en Kubernetes (OPS) - Minikube
Revisar la imagen `evidence/paso6(despliegue).png`



