# Actividad 22 (Observabilidad y Telemetría con Prometheus, Loki, Tempo y MCP)

Luis Andre Trujillo Serva (20220428D)

## 1. Preparación técnica
Cabe mencionar que realizamos una modificación en el `Makefile` , ya que cuento con la versión **V1** de Docker , por lo tanto habrá modificaciones de `docker compose` por `docker-compose`.

## 2. Levantar el stack y generar telemetría

### Servicios Levantados

| Servicio | URL | Estado |
|----------|-----|--------|
| FastAPI App | http://localhost:8000/docs | Listo |
| Prometheus | http://localhost:9090 | Listo |
| Grafana | http://localhost:3000 | Credenciales: admin/devsecops |
| Loki | http://localhost:3100 | Solo API |
| Tempo | http://localhost:3200 | Solo API |
| MCP Server | http://localhost:8080/docs | Listo |

## 3. Parte A - Observabilidad y tipos de telemetría

### Parte A - Observabilidad y Telemetría

- `observabilidad-telemetria.md`: Explicación de diferencias entre monitoreo y observabilidad, tipos de telemetría en el stack, y diagrama de flujo completo.

## 4. Parte B - Métricas con Prometheus y PromQL


