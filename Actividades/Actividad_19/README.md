# Actividad 19
Luis Andre Trujillo Serva
## Conceptualización de microservicios

### ¿Por qué microservicios?

#### Evolución : Monolito -> SOA -> Microservicios

**Monolito**:

- **Arquitectura**: Una sola aplicación que contiene todas las funcionalidades
- **Características**: Código fuertemente acoplado, base de datos única, despliegue único
- **Ventajas**: Desarrollo simple, debugging fácil, transacciones ACID
- **Desventajas**: Se convierte en "big ball of mud", despliegues riesgosos, escalado ineficiente

**SOA (Service-Oriented Architecture)**:

- **Arquitectura**: Servicios empresariales reutilizables con ESB (Enterprise Service Bus)
- **Características**: Servicios más grandes, comunicación SOAP/WS-*, ESB como punto central
- **Ventajas**: Reutilización, integración empresarial
- **Desventajas**: ESB como cuello de botella, complejidad de governance, acoplamiento tecnológico

**Microservicios**:

- **Arquitectura**: Servicios pequeños, independientes, orientados a capacidades de negocio
- **Características**: Despliegue independiente, APIs REST/gRPC, bases de datos descentralizadas
- **Ventajas**: Escalado granular, autonomía de equipos, resiliencia
- **Desventajas**: Complejidad distribuida, consistencia eventual

#### Casos donde el monolito se vuelve costoso de operar

**Caso 1: E-commerce con Picos Estacionales (Black Friday)**

Problemas del monolito:

- Escalado ineficiente: Todo el sistema escala aunque solo el módulo de inventario tenga carga
- Recursos desperdiciados: Servidores de pago sobredimensionados durante picos de búsqueda
- Riesgo de caída total: Un error en recomendaciones puede afectar checkout
- Coste operacional: Infraestructura siempre dimensionada para el pico máximo

Solución con microservicios:

- Escalar solo servicio de inventario durante Black Friday
- Servicio de búsqueda independiente para ofertas flash
- Servicio de pago aislado y estable

**Caso 2: SaaS Multi-tenant con Requerimientos Diversos**

Problemas del monolito:

- Deployments riesgosos: Actualización afecta a todos los clientes simultáneamente
- Customización compleja: Modificaciones para un cliente rompen funcionalidad para otros
- Rendimiento impredecible: Un tenant "ruidoso" afecta el performance global
- Evolución bloqueada: No se puede modernizar tecnología por dependencias cruzadas

Solución con microservicios:

- Servicios por vertical: CRM separado de facturación, separado de analytics
- Deployments selectivos: Actualizar módulo de reporting sin tocar core
- Escalado por tenant: Recursos dedicados para clientes enterprise
- Evolución independiente: Migrar servicios individualmente a nuevas tecnologías

### Definiciones clave

#### Microservicio

- Unidad de despliegue independiente: Puede desplegarse sin afectar otros servicios
- Una capacidad de negocio: Ej: "Gestión de usuarios", "Procesamiento de pagos", "Catálogo de productos"
- Contrato definido por API: Interfaces claras via REST, gRPC, o mensajería
- Ejemplo: Servicio de "Notificaciones" responsable únicamente de enviar emails/SMS

#### Aplicación de Microservicios

- Colección de servicios: Conjunto coordinado que forma una aplicación completa
- Gateway/API Gateway: Punto único de entrada, enrutamiento, autenticación
- Balanceo de carga: Distribución eficiente de tráfico entre instancias
- Observabilidad:
    - Métricas: Rendimiento, latencia, errores (Prometheus)
    - Logs: Trazabilidad de requests (ELK Stack)
    - Trazas: Flujo completo entre servicios (Jaeger/Zipkin)

### Críticas al monolito

1. **Cadencia de Despliegue Reducida**

- Problema: Deployments infrecuentes (semanales/mensuales) por riesgo alto
- Causa: Cambio pequeño requiere testing y deploy de toda la aplicación
- Impacto: Time-to-market lento, feedback retardado
- Ejemplo: Corregir typo en UI requiere deploy completo con downtime

2. **Acoplamiento que Impide Escalado Independiente**

- Problema: No se puede escalar componentes individuales
- Causa: Dependencias fuertes entre módulos
- Impacto: Recursos desperdiciados, performance subóptimo
- Ejemplo: CPU para procesamiento de imágenes compartida con lógica de negocio

### Popularidad y Beneficios
Por qué Empresas Grandes los adoptaron:

**Netflix**:

- Aislamiento de fallos: Un servicio caído no afecta streaming
- Escalado granular: Escalar recomendaciones independientemente de reproducción
- Autonomía de equipos: 100+ equipos desarrollando simultáneamente

**Amazon**:

- Two-pizza teams: Equipos pequeños y autónomos
- Despliegue continuo: Miles de deployments diarios
- Innovación acelerada: Pruebas A/B a nivel de servicio

**Uber**:

- Crecimiento global: Servicios regionales independientes
- Resiliencia: Fallo en pagos no afecta viajes activos
- Evolución tecnológica: Migrar gradualmente de monolitos

### Desventajas y retos

**Desafíos principales**

1. Redes/Seguridad:

- Comunicación inter-servicios vulnerable
- Surface attack ampliado
- Latencia de red impredecible

2. Orquestación:

- Gestión compleja de múltiples servicios
- Discovery service, configuración distribuida
- Health checking y auto-recovery

3. Consistencia de Datos:

- Transacciones distribuidas complejas
- Consistencia eventual vs ACID
- Sincronización entre bases de datos

4. Testing Distribuido:

- Pruebas de integración complejas
- Dependencias externas en testing
- Debugging cross-service difícil

**Mitigaciones**

- OpenAPI/Contratos: Especificaciones formales de APIs
- Pruebas Contractuales: Pact testing entre consumidor-proveedor
- Trazabilidad (Jaeger): Distributed tracing para debugging
- Patrones de Sagas: Manejo de transacciones largas distribuidas

### Principios de diseño

**DDD (Domain Driven Design)**

- Límites contextuales: Dividir por subdominios de negocio
- Lenguaje ubicuo: Términos de negocio compartidos
- Contextos delimitados: Ej: "ShippingContext", "PaymentContext", "InventoryContext"
- Ejemplo: No dividir por "base de datos usuarios" sino por "gestión de identidad"

**DRY en Microservicios**

- Balance crítico: Librerías comunes vs acoplamiento
- Duplicación aceptable: Código similar en servicios diferentes
- Librerías estratégicas: Solo para concerns transversales (logging, auth)
- Anti-patrón: Shared library que obliga deployments coordinados

**Criterios de Tamaño**

- Capacidad de negocio: "Gestionar inventario" vs "tabla inventory"
- Equipo autónomo: Servicio mantenible por 2-3 developers
- Independencia de despliegue: Cambios sin coordinar con otros equipos
- Evitar dogmas: No "una tabla por servicio", sino "un bounded context por servicio"
  
### Conclusiones y decisiones de diseño

**Decisiones Clave para Nuestra Implementación**

1. Límites por Capacidad de Negocio:

- Servicio de "Items" (catálogo) separado de "Orders" (pedidos)
- Cada servicio con su propia base de datos SQLite

2. Independencia de Despliegue:

- Versionado semántico estricto (SemVer)
- Contratos API bien definidos
- Servicios desplegables individualmente

3. Observabilidad desde el Inicio:

- Logs estructurados
- Métricas básicas de salud
- Ready para distributed tracing

4. Tolerancia a Fallos:

- Design for failure
- Circuit breakers en comunicaciones
- Fallback strategies

**Ejemplo de Aplicación**

Para nuestra actividad, diseñaremos:

- Servicio de Items: Gestión de catálogo de productos
- API Gateway: Enrutamiento único
- Base de datos independiente: SQLite por servicio
- Comunicación: APIs REST con contratos claros

**Justificación**: Esta separación permite evolucionar el catálogo independientemente de otros módulos futuros (usuarios, pedidos, pagos), manteniendo la simplicidad operacional con SQLite para la base obligatoria.

