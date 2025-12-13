# Actividad 22 - Observabilidad y Tipos de Telemetría

## Diferencia entre Monitoreo y Observabilidad

### Monitoreo
El **monitoreo** es un enfoque reactivo y basado en métricas predefinidas para verificar el estado conocido de un sistema. Se centra en responder a la pregunta: **"¿Está el sistema funcionando según lo esperado?"**

**Características del monitoreo:**
- Basado en métricas e indicadores conocidos
- Enfoque en thresholds (umbrales) y alertas predefinidas
- Respuesta a condiciones esperadas y problemas conocidos
- Ejemplo: Alertar cuando el uso de CPU supera el 80%

### Observabilidad
La **observabilidad** es un enfoque proactivo que permite entender el estado interno de un sistema a partir de sus salidas externas. Responde a la pregunta: **"¿Por qué el sistema se comporta de esta manera?"**

**Características de la observabilidad:**
- Capacidad de investigar problemas desconocidos
- Triada fundamental: Métricas, Logs y Trazas
- Enfoque en exploración y descubrimiento
- Permite hacer preguntas ad-hoc sobre el sistema

**Relación:** El monitoreo es un subconjunto de la observabilidad. Mientras el monitoreo te dice *qué* está mal, la observabilidad te ayuda a entender *por qué*.

## Tipos de Telemetría en el Stack Observabilidad-mcp

### 1. Métricas (Prometheus / OpenTelemetry)
**Definición:** Mediciones numéricas cuantitativas que representan el estado del sistema en un punto específico en el tiempo.

**Ejemplos en nuestro stack:**
- `http_server_requests_total`: Contador de solicitudes HTTP
- `http_server_duration_seconds`: Histograma de latencia
- `up`: Estado de los servicios (1=up, 0=down)

**Características:**
- **Series temporales** con etiquetas (labels)
- **Bajo costo** de almacenamiento
- Tipos principales:
  - **Counter**: Solo incrementa (ej: número de requests)
  - **Gauge**: Sube y baja (ej: uso de memoria)
  - **Histogram**: Distribución de valores (ej: latencias)

### 2. Logs (Loki)
**Definición:** Registros de eventos estructurados o no estructurados que capturan información específica sobre la ejecución del sistema.

**Ejemplos en nuestra app:**
- `"GET /api/v1/items HTTP/1.1" 200`
- `"ERROR: Division by zero in work endpoint"`
- `"User authentication successful"`

**Características:**
- **Alto volumen** de datos
- **Indexación por etiquetas** para búsqueda eficiente
- **Contexto rico** pero no estructurado
- Pueden contener datos sensibles (necesita saneamiento)

### 3. Trazas Distribuidas (Tempo)
**Definición:** Registro del camino completo de una solicitud a través de múltiples servicios, mostrando la jerarquía y duración de cada operación.

**Ejemplos en nuestro stack:**
- Trace completo de una petición a `/api/v1/work`
- Relación padre-hijo entre spans
- Tiempos de ejecución por cada componente

**Características:**
- **Jerarquía de spans**: trace → span → subspan
- **Contexto distribuido**: trace-id, span-id
- **Mapeo de dependencias** entre servicios
- **Propagación de contexto** vía headers HTTP

### 4. Otros Tipos de Telemetría (No implementados en este stack)

#### Eventos de Negocio
- Eventos discretos significativos para el negocio
- Ejemplo: `usuario_registrado`, `pago_procesado`, `pedido_entregado`
- Útiles para análisis de comportamiento y auditoría

#### Profiling (Perfilado de Rendimiento)
- Análisis detallado del rendimiento a nivel de código
- Ejemplos: hotspots de CPU, uso de memoria, bloqueos
- Herramientas: Pyroscope, Parca, pprof

#### Heartbeats / Health Checks
- Verificaciones periódicas de disponibilidad
- Latencia desde puntos de red específicos
- Útiles para SLAs y SLOs

#### Métricas de Negocio
- Métricas que conectan el rendimiento técnico con resultados de negocio
- Ejemplos: conversiones por segundo, ingresos por usuario activo

## Relación entre Componentes

### 1. App → OTEL Collector
La aplicación FastAPI está instrumentada con OpenTelemetry SDK, que:
- Exporta métricas vía OTLP (OpenTelemetry Protocol)
- Escribe logs a stdout (recogidos por Promtail)
- Genera trazas distribuidas con contexto propagation

### 2. OTEL Collector → Backends de Telemetría
El collector actúa como router inteligente:
- **Métricas** → Prometheus (scrape endpoint en :8889)
- **Logs** → Loki (vía Promtail que escucha stdout)
- **Trazas** → Tempo (vía OTLP gRPC)

### 3. Grafana como Punto Unificado
Grafana se conecta a los tres backends:
- **Prometheus Data Source**: Para consultas PromQL
- **Loki Data Source**: Para consultas LogQL  
- **Tempo Data Source**: Para consultas TraceQL

### 4. MCP Server como Resumen
El servidor MCP proporciona:
- Endpoint `/api/summary` que agrega datos de los tres pilares
- Formato estructurado para consumo por LLMs/agentes
- Puente entre observabilidad técnica y análisis de IA


