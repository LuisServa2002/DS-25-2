# Actividad 01
Luis Andre Trujillo Serva

Realizado en 5 horas.
## 4.1 DevOps vs. cascada tradicional
La siguiente estructura fue creada por mi persona a partir de [DevOps vs Cascada Tradicional vs Agile](https://abhaykarthik.medium.com/waterfall-vs-agile-vs-devops-sdlc-models-8cc11b1a6edc).
| Característica               | Waterfall (Cascada)                                                                 | DevOps                                                                                      |
|-------------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Enfoque**                   | El modelo en cascada proporciona un enfoque secuencial lineal para gestionar proyectos de software. Cada fase depende de los entregables de la fase anterior. | DevOps es una metodología ágil que abarca Desarrollo (Dev) y Operaciones (Ops). Permite la entrega de extremo a extremo del ciclo de vida de funciones, correcciones y actualizaciones en intervalos frecuentes. |
| **Año**                       | 1970                                                                                 | 2009                                                                                        |
| **Alcance y Cronograma**      | Ajusta el cronograma para preservar el alcance. Requerimientos fijos. Flexibilidad limitada. | Ajusta el alcance para preservar el cronograma. Altamente sensible a las necesidades del negocio. |
| **Tiempo de salida al mercado** | Lento                                                                                 | Continuo                                                                                    |
| **Automatización**            | Baja                                                                                  | Alta                                                                                        |
| **Retroalimentación del cliente** | Al final del proyecto                                                                    | Continua                                                                                    |
| **Calidad**                   | Baja. Los problemas se identifican solo en la etapa de pruebas.                       | Alta. Pruebas unitarias automatizadas durante el desarrollo.                                |
| **Colaboración**              | Los equipos trabajan en silos.                                                        | Todas las partes interesadas están involucradas de principio a fin.                        |
| **Variaciones**               | Modelo en V                                                                           | CI/CD, DevSecOps                                                                            |
### ¿Por qué DevOps acelera y reduce riesgo en software para la nube frente a cascada?
  
DevOps acelera y reduce el riesgo en software para la nube porque permite entregas continuas con integración y despliegue automático, detectando errores tempranamente gracias a pruebas automatizadas. A diferencia del modelo en cascada, donde el cliente solo ve el producto al final, en DevOps la retroalimentación es constante y los cambios se adaptan rápido a las necesidades. Además, la colaboración entre desarrollo y operaciones, junto con la escalabilidad de la nube, agiliza los despliegues y disminuye el riesgo de fallos en producción.

### Pregunta retadora
  
Un contexto real donde un enfoque cercano a cascada sigue siendo razonable es en el desarrollo de sistemas médicos (por ejemplo, software para equipos de diagnóstico o monitoreo de pacientes). En este tipo de proyectos, cada fase debe completarse y documentarse antes de avanzar, porque la certificación regulatoria exige pruebas exhaustivas y trazabilidad completa.

#### Criterios verificables:

1. Cumplimiento normativo: el software debe ajustarse a estándares , lo que requiere documentación formal y validación de cada etapa.

2. Integración con hardware crítico: el sistema depende de dispositivos médicos o financieros ya validados, donde cambios frecuentes serían costosos o arriesgados.

#### Trade-offs:

1. Se sacrifica velocidad de entrega porque el ciclo de vida es rígido y secuencial.

2. Se gana en conformidad y seguridad, reduciendo riesgos legales, regulatorios y de fallos que podrían afectar vidas humanas o la estabilidad financiera.

## 4.2 Ciclo tradicional de dos pasos y silos (limitaciones y anti-patrones)
Una imagen referencial acerca de **silos organizacionales** se encuentra ubicado en `imagenes/silos-equipos.jpeg`.
### Limitaciones del ciclo "construcción -> operación" sin integración continua
1. Grandes lotes de cambios acumulados:
Al no integrar ni desplegar de forma continua, el software se acumula en bloques grandes que se entregan de una sola vez. Esto aumenta el costo de integración tardía, porque aparecen conflictos y errores difíciles de rastrear cuando finalmente se juntan las partes.

2. Colas de defectos y retrasos en la retroalimentación:
Los problemas de calidad suelen detectarse tarde, muchas veces en la fase de operación. Esto genera largas colas de defectos que se van acumulando y producen retrabajos, incrementando los tiempos de entrega y alargando el MTTR (Mean Time to Recovery) cuando ocurre un incidente.

### Pregunta retadora: anti-patrones que agravan incidentes

- Anti-patrón 1: "Throw over the wall"
Consiste en que el equipo de desarrollo entrega el software al área de operaciones sin acompañamiento ni responsabilidad compartida, como si “lanzara el producto por encima del muro”.

Esto genera handoffs (traspasos) con pérdida de contexto y asimetrías de información, porque los desarrolladores conocen el código pero los operadores no.

El resultado es un mayor MTTR (tiempo medio de recuperación) ante incidentes, ya que los operadores deben investigar desde cero problemas que el equipo de desarrollo podría resolver más rápido.

- Anti-patrón 2: Seguridad como auditoría tardía
La seguridad se revisa al final del ciclo, como una “auditoría” en vez de un proceso continuo.

Esto implica un alto costo de integración tardía, porque cuando se descubren vulnerabilidades es necesario rehacer partes significativas del sistema.

Agrava los retrabaos y favorece degradaciones repetitivas, ya que los mismos problemas pueden reaparecer en versiones futuras si no se corrigen de raíz durante el desarrollo.

## 4.3 Principios y beneficios de DevOps (CI/CD, automatización, colaboración; Agile como precursor)

### Describe CI y CD destacando tamaño de cambios, pruebas automatizadas cercanas al código y colaboración.
La **Integración Continua (CI)** consiste en realizar cambios pequeños y frecuentes en el código, integrándolos en un repositorio compartido. Cada integración activa pruebas automatizadas cercanas al código, lo que permite detectar fallos temprano y reducir el costo de corrección. Además, la CI promueve la colaboración constante, ya que los desarrolladores deben alinear sus cambios con los del resto del equipo para evitar conflictos.

La **Entrega Continua (CD)** extiende este proceso, automatizando la entrega hacia entornos de prueba o producción. Garantiza que cada cambio probado pueda ponerse en producción de forma confiable y rápida, reduciendo el riesgo de errores acumulados y aumentando la capacidad de respuesta del negocio. CD aporta mayor confianza, ya que el software siempre se mantiene en un estado desplegable.

### Explica cómo una práctica Agile (reuniones diarias, retrospectivas) alimenta decisiones del pipeline (qué se promueve, qué se bloquea).
Las prácticas Agile fomentan ciclos cortos de retroalimentación que nutren el pipeline de CI/CD.  
- En las **reuniones diarias (daily stand-ups)** los equipos identifican bloqueos que pueden traducirse en detener la promoción de un cambio en el pipeline hasta que el problema se resuelva.  
- En las **retrospectivas**, los equipos analizan qué funcionó y qué no, ajustando reglas de calidad (tests más estrictos, linting, cobertura de código, umbrales de seguridad) que luego se integran directamente en las etapas de CI/CD.  

De esta manera, Agile guía qué cambios se promueven y cuáles se bloquean, alineando la cultura de mejora continua con la automatización y la colaboración.

### Propón un indicador observable (no financiero) para medir mejora de colaboración Dev-Ops.
Un indicador útil es el **tiempo promedio desde que un Pull Request está listo hasta que se despliega en el entorno de pruebas**. Este refleja la fluidez de la colaboración entre desarrollo y operaciones: si disminuye, significa que existe menos fricción, handoffs más rápidos y mayor integración cultural.  

Otro indicador relevante es la **proporción de despliegues que requieren rollback sin downtime**, ya que muestra la capacidad de recuperación ágil del sistema y la efectividad de la comunicación entre los equipos Dev y Ops.

## 4.4 Evolución a DevSecOps (seguridad desde el inicio: SAST/DAST; cambio cultural)
### Diferencia SAST (estático, temprano) y DAST (dinámico, en ejecución), y ubícalos en el pipeline.
- SAST (Static Application Security Testing): Analiza el código fuente o binario antes de compilar. Permite identificar vulnerabilidades como inyecciones SQL, XSS, credenciales hardcodeadas, dependencias inseguras.
  - Se ubica en las primeras fases del pipeline (commit / build), integrándose con repositorios y herramientas de análisis automático.
  
- DAST (Dynamic Application Security Testing): Evalúa la aplicación en ejecución, simulando ataques externos para detectar brechas de seguridad reales en endpoints, APIs o configuración del servidor.
  - Se ubica en entornos de pruebas o staging, tras el despliegue de la aplicación en un entorno controlado.
  
De este modo, SAST actúa como una primera línea preventiva y DAST como una validación práctica antes de la entrega.
### Define un gate mínimo de seguridad con dos umbrales cuantitativos (por ejemplo, "cualquier hallazgo crítico en componentes expuestos bloquea la promoción"; "cobertura mínima de pruebas de seguridad del X%").
- **Bloqueo automático** de la promoción si se detecta al menos un hallazgo crítico en componentes expuestos (ej. API pública, login).
- **Cobertura mínima de pruebas de seguridad** ≥ 80%, medida en base a escaneos automatizados (SAST+DAST) y pruebas unitarias con casos de seguridad.
  
Esto asegura que solo avancen versiones que cumplen criterios mínimos de seguridad.
### Incluye una política de excepción con caducidad, responsable y plan de corrección.
En casos donde el bloqueo automático podría detener entregas críticas:
- Se puede autorizar una excepción temporal.
- Debe contar con:
  - **Fecha de caducidad definida** (ej. máximo 30 días).
  - **Responsable asignado** (dueño técnico o equipo de seguridad).
  - **Plan de corrección documentado** con hitos y compromisos de remediación.

Esto evita que las excepciones se vuelvan permanentes y obliga a la rendición de cuentas.

### Pregunta retadora: ¿cómo evitar el "teatro de seguridad" (cumplir checklist sin reducir riesgo)? Propón dos señales de eficacia (disminución de hallazgos repetidos; reducción en tiempo de remediación) y cómo medirlas.
El “teatro de seguridad” ocurre cuando se cumplen formalidades (checklists, reportes) pero sin impacto real en la reducción de riesgos. Para evitarlo:
- Señal 1: Disminución de hallazgos repetidos.
  - Medición: comparar el número de vulnerabilidades recurrentes entre releases (ej. reducción del 30% en hallazgos de inyección SQL en 3 meses).
- Señal 2: Reducción en el tiempo de remediación.
  - Medición: registrar el MTTR (Mean Time To Remediate) de fallas críticas, buscando que disminuya de semanas a días.

Con estas métricas, la seguridad se convierte en un valor medible y continuo, y no solo en un requisito burocrático.

## 4.5 CI/CD y estrategias de despliegue (sandbox, canary, azul/verde)
### Inserta una imagen del pipeline o canary en imagenes/pipeline_canary.png.
En la siguiente imagen mostramos el proceso del pipeline CI/CD.
**Imagen ubicada en: `imagenes/pipeline_canary.png`.

### Elige una estrategia para un microservicio crítico (por ejemplo, autenticación) y justifica.

Sabemos que un microservicio se divide en trabajos independientes por lo tanto , elejimos un **despliegue canario** , ya que el servicio de autenticación es crítico y cualquier error impacta directamente en el acceso de los usuarios.

Con el despliegue canario , podemos liberar gradualmente la nueva versión a un porcentaje controlado de tráfico (por ejemplo, 5%, luego 20%, y así sucesivamente), observando métricas clave antes de expandir al 100%. Esto permite:
- Detectar fallas sin afectar a todos los usuarios.
- Mitigar riesgos antes de que el cambio escale.
- Validar compatibilidad con clientes y servicios dependientes.

### Crea una tabla breve de riesgos vs. mitigaciones (al menos tres filas), por ejemplo:

  - Regresión funcional -> validación de contrato antes de promover.
  - Costo operativo del doble despliegue -> límites de tiempo de convivencia.
  - Manejo de sesiones -> "draining" y compatibilidad de esquemas.

|Riesgo|Mitigacion|
|------|----------|
|Regresión funcional|Validación de contrato y prueba automáticas antes de promover la versión|
|Costo operativo del doble despliegue|Definir un límite de convivencia(máx 24 horas) para reudicr gasto en recursos|
|Manejo de sesiones activas|Uso de session draining y esquemas de datos compatibles hacia atrás|

### Define un KPI primario (p. ej., error 5xx, latencia p95) y un umbral numérico con ventana de observación para promoción/abortado.
- Métrica: Latencia P95 en autenticación.
- Umbral: ≤ 300 ms.
- Ventana de observación: 15 minutos antes de promover al siguiente porcentaje de tráfico.

### Pregunta retadora: si el KPI técnico se mantiene, pero cae una métrica de producto (conversión), explica por qué ambos tipos de métricas deben coexistir en el gate.
Si el KPI técnico (latencia ≤ 300 ms) se mantiene estable, pero la métrica de producto (por ejemplo, conversión en login completado) cae, significa que el sistema funciona bien desde el punto de vista técnico, pero el cambio está afectando la experiencia del usuario o el negocio.

Por ejemplo: una actualización en la interfaz del flujo de login puede generar confusión y disminuir conversiones, aun cuando la API responde rápido y sin errores.

Por eso, ambos tipos de métricas (técnicas y de negocio) deben coexistir en el gate de promoción. Las métricas técnicas garantizan estabilidad operativa, mientras que las de producto aseguran que el cambio no dañe el valor entregado al usuario ni los objetivos del negocio.

## 4.6 Fundamentos prácticos sin comandos (evidencia mínima)
Realiza comprobaciones con herramientas estándar, pero no pegues los comandos. En el README escribe los hallazgos y la interpretación. Adjunta tus capturas en imagenes/ y marca los campos relevantes (códigos, cabeceras, TTL, CN/SAN, fechas, puertos).

1. HTTP - contrato observable
- **Método:** `GET`  
- **Código de estado:** `200 OK`  
- **Cabeceras clave:**  
  - `x-amzn-trace-id` → usada para trazabilidad de la petición en sistemas distribuidos.  
  - `user-agent` → identifica al cliente que realiza la petición (en este caso `PostmanRuntime/7.32.3`).  

  **Hallazgos e interpretación:**  
La respuesta `200 OK` confirma que el contrato HTTP se cumplió de manera correcta.  
Las cabeceras seleccionadas influyen directamente en:  
- **Observabilidad:** `x-amzn-trace-id` permite seguir la petición en un entorno distribuido, facilitando diagnóstico en caso de errores o latencias anómalas.  
- **Compatibilidad y auditoría:** `user-agent` indica qué cliente está consumiendo el servicio, lo que ayuda a detectar patrones de uso y posibles incompatibilidades.    

La evidencia se encuentra en `imagenes/http-evidencia.png`.
  
2. DNS - nombres y TTL
- Hallazgos:
    - **Dominio consultado**: www.kinsta.com
    - **Dirección IP resuelta**: 104.18.0.153
    - **Tipo de registro**: A (dirección IPv4)
    - **TTL observado**: 56 segundos (destacado en azul en la captura)

- Interpretación:

  El **TTL de 56 segundos** es relativamente bajo, lo que indica una estrategia de DNS agresiva para cambios frecuentes. Esto tiene implicaciones importantes:

  **Impacto en rollbacks y cambios de IP:**
  - **Propagación rápida**: Con TTL=56s, los cambios de IP se propagan en menos de 1 minuto, permitiendo rollbacks casi inmediatos
  - **Ventana de inconsistencia mínima**: Durante 56 segundos máximo, algunos clientes podrían resolver la IP antigua mientras otros ya tienen la nueva
  - **Mayor carga en servidores DNS**: TTL bajo significa más consultas DNS, ya que las respuestas se cachean por menos tiempo
  - **Flexibilidad operacional**: Ideal para arquitecturas cloud donde las IPs pueden cambiar dinámicamente o para mitigación rápida de incidentes

La evidencia se encuentra en `imagenes/dns-ttl.jpg`.

3. TLS - seguridad en tránsito

- Hallazgos:
  - **CN (Common Name)**: www.bbc.com
  - **Emisora**: GlobalSign RSA OV SSL CA 2018
  - **Vigencia**: 
    - **Válido desde**: 8/9/2021
    - **Válido hasta**: 9/10/2022
  - **Algoritmo de firma**: sha256RSA
  - **Número de serie**: 19c66b8e70c6db558de177e9

- Interpretación:

  **Validación de cadena de confianza:**
Si este certificado **no validara correctamente** la cadena, ocurriría:

    - **Errores de confianza**: El navegador mostraría advertencias de "conexión no segura" o "certificado no válido"
    - **Riesgo de MITM**: Sin validación adecuada, un atacante podría interceptar y modificar el tráfico usando un certificado falso
    - **Impacto en UX**: Los usuarios verían páginas de advertencia, reduciendo la confianza y conversión del sitio
    - **Bloqueo automático**: Navegadores modernos pueden rechazar completamente conexiones con certificados inválidos

  **Observaciones del certificado:**
    - **Emisor confiable**: GlobalSign es una CA reconocida mundialmente
    - **Validación organizacional (OV)**: Nivel intermedio de validación, más seguro que DV básico
    - **Algoritmo seguro**: SHA-256 con RSA es considerado criptográficamente seguro
    - **Vigencia adecuada**: Período de 1 año equilibra seguridad y gestión operacional  
  
La evidencia se encuentra en `imagenes/tls-cert.png`.

4. Puertos - estado de runtime

- Hallazgos:
**Dos puertos destacados en escucha:**

  1. **Puerto 445** (0.0.0.0:445)
   - **Servicio**: SMB/CIFS (Server Message Block)
   - **Función**: Compartición de archivos e impresoras en red Windows

  2. **Puerto 135** (0.0.0.0:135)
   - **Servicio**: RPC Endpoint Mapper
   - **Función**: Servicios de llamadas a procedimientos remotos de Windows

- Interpretación:

  **Detección de despliegues incompletos:**
  - **Puerto no expuesto**: Si una aplicación web debería escuchar en puerto 8080 pero no aparece en `netstat`, indica que el servicio no inició correctamente o tiene problemas de configuración
  - **Binding incorrecto**: Si aparece solo en 127.0.0.1:8080 en lugar de 0.0.0.0:8080, la aplicación no será accesible externamente

  **Detección de conflictos:**
  - **Puerto ocupado**: Si intentas desplegar en puerto 80 pero ya está en uso, el nuevo servicio fallará al iniciar
  - **Múltiples servicios**: Ver el mismo puerto usado por diferentes procesos indica conflicto de configuración

  **Observaciones adicionales:**
  - **Puertos dinámicos** (49664-50923): Servicios Windows temporales, normales en el sistema
  - **IPv6 habilitado**: Los puertos [::] indican que el sistema acepta conexiones IPv6
  - **Binding 0.0.0.0**: Servicios disponibles en todas las interfaces de red

  **Diagnóstico operacional:**
Esta evidencia permite identificar rápidamente si los servicios esperados están activos y accesibles, crucial para troubleshooting de conectividad.

La evidencia se encuentra en `imagenes/puertos.png`.


5. 12-Factor - port binding, configuración, logs
- **Parametrización del puerto:** el servicio no debe tener el puerto escrito en el código fuente. En su lugar, se define como **variable de entorno** (`PORT=8080`), lo que permite que distintos entornos (dev, staging, prod) usen configuraciones diferentes sin cambios de código.  
- **Logs en ejecución:** los logs deben enviarse a **stdout/stderr**, de modo que el runtime (Docker, Kubernetes, systemd) los capture, rote y almacene centralizadamente.  
  - Esto asegura trazabilidad y evita depender de archivos locales que se pueden perder o saturar disco.  
- **Anti-patrón:** incluir credenciales en el código fuente (ej. claves API hardcodeadas).  
  - **Impacto:** rompe reproducibilidad (funciona solo en un entorno), expone seguridad y obliga a redeploys innecesarios al cambiar credenciales.  

6. Checklist de diagnóstico (incidente simulado)

**Escenario:** usuarios reportan intermitencia.  
Objetivo: discriminar si la causa está en HTTP, DNS, TLS o puertos.

---

#### Paso 1: Verificar contrato HTTP
- **Objetivo:** comprobar si el servicio responde con el método y código esperados.
- **Evidencia esperada:** respuesta con código **200 OK** (o el definido en contrato), más cabeceras clave.
- **Interpretación:**  
  - Si devuelve error **5xx** → posible fallo de aplicación/backend.  
  - Si devuelve error **4xx** → contrato roto o endpoint incorrecto.  
- **Acción siguiente:** si no hay respuesta válida, escalar al equipo de aplicación; si responde bien, continuar con DNS.

---

#### Paso 2: Validar resolución DNS
- **Objetivo:** confirmar que el dominio resuelve a las IPs correctas en distintos resolvers.
- **Evidencia esperada:** registro **A** o **CNAME** consistente en varias consultas, con TTL razonable.
- **Interpretación:**  
  - Si las IPs difieren o algunas consultas fallan → inconsistencia en propagación DNS.  
  - Si todo coincide → continuar con TLS.  
- **Acción siguiente:** si hay inconsistencia, revisar configuración DNS o esperar propagación.

---

#### Paso 3: Revisar certificado TLS
- **Objetivo:** verificar que el certificado no esté caducado y que los campos CN/SAN correspondan al dominio.
- **Evidencia esperada:** certificado válido, dentro de vigencia, emitido por CA de confianza.
- **Interpretación:**  
  - Si el certificado está vencido o mal emitido → error de confianza, riesgo de MITM, usuarios afectados.  
  - Si es válido → continuar con puertos.  
- **Acción siguiente:** renovar/reemitir certificado en caso de fallo.

---

#### Paso 4: Comprobar puertos expuestos
- **Objetivo:** verificar que el servicio escucha en el puerto esperado (ej. 80/443).
- **Evidencia esperada:** puerto en **LISTENING** en el servidor, accesible desde cliente.
- **Interpretación:**  
  - Si el puerto no está abierto → despliegue incompleto o firewall bloqueando.  
  - Si está abierto → continuar con runtime.
- **Acción siguiente:** corregir configuración de servicio/firewall si no está expuesto.

---

#### Paso 5: Revisión de logs de aplicación
- **Objetivo:** correlacionar eventos de error en logs con los tiempos de los reportes de intermitencia.
- **Evidencia esperada:** trazas de error, timeouts, o saturación en el servicio.
- **Interpretación:**  
  - Si hay errores frecuentes → bug o sobrecarga en aplicación.  
  - Si no hay errores → seguir con pruebas de carga.  
- **Acción siguiente:** escalar al equipo de desarrollo/ops con logs para análisis.

---

#### Paso 6: Validación post-reversión (si aplica)
- **Objetivo:** comprobar estabilidad tras rollback o mitigación temporal.
- **Evidencia esperada:** métricas de error reducidas, latencia estable, logs sin anomalías.
- **Interpretación:**  
  - Si la estabilidad se recupera → incidente mitigado, seguir con análisis de causa raíz.  
  - Si persiste la intermitencia → escalar como incidente mayor (mayor prioridad).  


## 4.7 Desafíos de DevOps y mitigaciones
- Inserta un diagrama propio o ilustración en imagenes/desafios_devops.png con tres desafíos anotados (culturales, técnicos, de gobernanza).

El diagrama creado se encuentra en `imagenes/desafios_devops.png`
- Enumera tres riesgos con su mitigación concreta (rollback, despliegues graduales, revisión cruzada, límites de "blast radius").
  
| Riesgo                                    | Mitigación concreta                                          |
|-------------------------------------------|--------------------------------------------------------------|
| Error crítico en despliegue de producción | **Rollback automatizado** al último estado estable.          |
| Impacto alto de cambios en todo el sistema | **Despliegues graduales (canary/blue-green)** para aislar impacto. |
| Sesgos o errores humanos en revisiones    | **Revisión cruzada de código** y límites de *blast radius* (afectar solo un subconjunto de usuarios). |

- Diseña un experimento controlado para validar que el despliegue gradual reduce riesgo frente a uno "big-bang": define métrica primaria, grupo control, criterio de éxito y plan de reversión.

**Hipótesis:** un despliegue gradual (canary) reduce incidentes críticos comparado con un despliegue "big-bang".  

1. **Métrica primaria:** tasa de errores **5xx** y latencia **p95** en los primeros 30 minutos post-despliegue.  
2.  **Grupo control:** una versión desplegada con enfoque *big-bang* (100% de usuarios al mismo tiempo).  
3.  **Grupo experimental:** la misma versión desplegada con estrategia *canary* (10% de usuarios iniciales, escalado progresivo).  
4.  **Criterio de éxito:** si el canary muestra **≥30% menos errores críticos** y mantiene latencia bajo 300 ms en la ventana de observación, se considera la estrategia más segura.
5.  **Plan de reversión:** si los umbrales se exceden, se revierte automáticamente a la versión estable anterior, con monitoreo intensivo hasta validar estabilidad.  


## 4.8 Arquitectura mínima para DevSecOps (HTTP/DNS/TLS + 12-Factor)
- Dibuja un diagrama propio en imagenes/arquitectura-minima.png con el flujo: Cliente -> DNS -> Servicio (HTTP) -> TLS, e indica dónde aplicar controles (políticas de caché, validación de certificados, contratos de API, límites de tasa).

El diagrama creado se encuentra en `imagenes/arquitectura-minima.png`.
- Explica cómo cada capa contribuye a despliegues seguros y reproducibles.
    - DNS: Al separar nombre de IP, puedes migrar de infraestructura (blue/green) sin cambiar clientes; con TTLs adecuados, controlas la velocidad de conmutación y reduces riesgos de rutas obsoletas. 
    - HTTP + caché: Políticas claras (Cache-Control, ETag) hacen los despliegues predecibles (clientes reusan artefactos versionados) y minimizan picos de tráfico tras releases. 
    - Contratos de API: CI/CD valida compatibilidad consumidor↔proveedor antes de liberar; evitas regresiones entre microservicios y reduces blast radius. 
    - TLS: Cifrado y autenticación end-to-end; con controles de validez/hostname y (opcional) mTLS para east-west traffic. 
    - Rate limiting: Mantiene el servicio estable ante abuso o bugs del cliente; métrica observable para gates de promoción. 
 
- Relaciona dos principios 12-Factor (config por entorno; logs a stdout) con evidencias operativas que un docente podría revisar (por ejemplo, diffs mínimos entre entornos, trazabilidad de logs).
    - Config (III): “Store config in the environment”
        - Qué es: la configuración vive fuera del código (variables de entorno / secrets), permitiendo el mismo build en dev/staging/prod. 
        - Evidencias:
            - Diffs mínimos entre entornos: el artefacto (imagen) es igual; sólo cambian ENV VARs (ver manifests de despliegue o kubectl describe/docker inspect).
            - Ausencia de secrets en el repo; presencia de env vars definidas en el runtime (p. ej., ConfigMap/Secrets). 

    - Logs (XI): “Treat logs as event streams”
        - Qué es: la app escribe a stdout; el plumbing (driver/agent) centraliza (ELK/OTel). Esto facilita trazabilidad por versión deploy. 
        - Evidencias revisables:
            - Registros accesibles sin entrar al pod (p. ej., kubectl logs o panel centralizado).
            - Correlación por trace/span ID y etiqueta de release (verifica en los metadatos del log).
