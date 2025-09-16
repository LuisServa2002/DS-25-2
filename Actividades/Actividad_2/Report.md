# Actividad 02
## 1.HTTP: Fundamentos y herramientas
1. Para **levantar la app** debemos descargar el archivo `Respuestas-actividad2.sh` y antes de ejecutarlo brindar permisos.
<p align="center">
    <img src="imagenes/http-levantar.png" width=500px height=100px>
<p/>
Se ha creado el entorno virtual y luego podemos ejecutar el app.py.
<p align="center">
    <img src="imagenes/http-ejecutar.png" width=500px height=150px>
<p/>

Abrimos una nueva terminal y realizamos el paso siguiente:

1. Inspección con `curl`:
- `curl -v http://127.0.0.1:8080/`
<p align="center">
    <img src="imagenes/http-paso2(1).png" width=500px height=200px>
<p/>

- `curl -i -X POST http://127.0.0.1:8080/` , Visualizamos la respuesta `405 Method Not Allowed` ya que la ruta existe pero no acepta el método **POST** ya que la app solo definio **GET**. Obtendriamos el error `404 Not Found` si la ruta no existiera.
<p align="center">
    <img src="imagenes/http-paso2(2).png" width=500px height=200px>
<p/>

- Respuesta a la pregunta : Nada cambia cuando se encuentra en ejecución , porque `miapp/app.py` lee `APP_MESSAGE` y `APP_RELEASE` desde `os.environ` al iniciar (variables asignadas a variables globales al cargar el módulo). Cambiar las variables de entorno en otra shell no modifica el entorno del proceso que ya está corriendo. Para que una nueva variable afecte a la app hay que reiniciar el proceso (o reimplementar lectura dinámica de configuración).
  
3. Puertos abiertos con `ss`:
   
<p align="center">
    <img src="imagenes/http-paso3.png" width=500px height=150px>
<p/>

`LISTEN` : el estado del socket (esperando conexiones).

`0.0.0.0:8080` : dirección y puerto en el que escucha (todas las interfaces IPv4 en el puerto 8080).

`users:(("python3",pid=12345,fd=3))`: identifica el proceso responsable.

4. Logs como flujo
<p align="center">
    <img src="imagenes/http-logs.png" width=700px height=200px>
<p/>

No se escriben en archivo porque, según 12-Factor, es más conveniente dividir tareas: la aplicación produce los logs, pero no se encarga de almacenarlos. En su lugar, los emite a stdout/stderr y el sistema (systemd, Docker, Kubernetes, etc.) se encarga de recolectarlos, rotarlos y almacenarlos. Esto mejora el despliegue, la portabilidad y la distribución de responsabilidades.

## 2.DNS: nombres, registros y caché
1. Host local 

Mediante el target logramos agregar y se evidencia en el siguiente `.txt`.
<p align="center">
    <img src="imagenes/DNS-parte01.png" width=700px height=100px>
<p/>
<p align="center">
    <img src="imagenes/DNS-parte01-respuesta.png" width=700px height=100px>
<p/>

2. Comprobando resolución

Al comprobar , se generan los siguientes `.txt` en la carpeta de evidencias.
<p align="center">
    <img src="imagenes/DNS-comprobar.png" width=700px height=100px>
<p/>
<p align="center">
    <img src="imagenes/DNS-parte02.png" width=700px height=100px>
<p/>

3. TTL/caché

Si haces varias consultas seguidas, el TTL va bajando hasta llegar a 0; luego el resolver vuelve a consultar al servidor autoritativo.
Esto evita sobrecarga en servidores y mejora la latencia, pero puede retrasar la propagación de cambios de DNS.
<p align="center">
    <img src="imagenes/DNS-parte03.png" width=700px height=300px>
<p/>

4.  Pregunta

Incluso ya hay una explicación generada por el archivo en `evidencias/4--10-hosts-vs-authoritative.txt`.

/etc/hosts es un archivo local estático que el sistema consulta antes de recurrir al DNS. No soporta TTL ni delegación.
Una zona DNS autoritativa vive en servidores que publican registros válidos para un dominio con TTLs y jerarquía.
En laboratorio, /etc/hosts sirve porque te permite simular un nombre de dominio resolviendo siempre a 127.0.0.1 sin necesidad de modificar servidores DNS públicos.

## 3.TLS: seguridad en tránsito con Nginx como reverse proxy
1. Certificado de laboratorio: 

Si volvemos a abrir WSL , necesitamos darle permiso a nuestro archivo `Respuestas-actividad2.sh` , a continuación mediante el comando `tls-cert` , se crean la carpeta certs donde genera el certificado autofirmado.
<p align="center">
    <img src="imagenes/TLS-parte01.png" width=700px height=200px>
<p/>

2. Configura Nginx:

<p align="center">
    <img src="imagenes/TLS-parte02.png" width=700px height=100px>
<p/>

3. Valida el handshake:

<p align="center">
    <img src="imagenes/TLS-parte03(handshake).png" width=700px height=100px>
<p/>

Luego , genera los siguientes archivos `.txt` en la carpeta de evidencias.
<p align="center">
    <img src="imagenes/TLS-parte03(txt).png" width=700px height=100px>
<p/>

El parámetro `-k` en curl permite ignorar la validación de la cadena de confianza del certificado. Esto es necesario porque nuestro certificado es autofirmado y no está emitido por una CA reconocida por el sistema.

4. Puertos y logs:

<p align="center">
    <img src="imagenes/TLS-parte04.png" width=700px height=100px>
<p/>

<p align="center">
    <img src="imagenes/TLS-parte04(2).png" width=700px height=100px>
<p/>

El socket de Flask se mantiene en 127.0.0.1:8080 y es accesible solo localmente.
Nginx escucha en :443, recibe las conexiones HTTPS, termina el TLS y luego reenvía el tráfico por HTTP interno hacia Flask en 127.0.0.1:8080.
Esto asegura que el cliente externo siempre entra cifrado por TLS, mientras que la comunicación entre Nginx y Flask queda dentro del mismo host.

## 4. 12-Factor App: port binding, configuración y logs
Vamos a demostrar estos tres principios clave de la app.
### Port binding: muestra que la app escucha en el puerto indicado por PORT (evidencia ss).
Levantamos la app mediante un puerto especifico :
<p align="center">
    <img src="imagenes/demostracion-parte01.png" width=700px height=100px>
<p/>
<p align="center">
    <img src="imagenes/demostracion-parte01(2).png" width=700px height=100px>
<p/>

### Config por entorno: ejecuta dos veces con distintos MESSAGE/RELEASE y documenta el efecto en la respuesta JSON.
Realizamos dos ejecuciones con variables distintas y obtenemos las respuestas de tipo JSON mediante el comando `curl http://127.0.0.1:8080/`:
<p align="center">
    <img src="imagenes/demostracion-parte02.png" width=700px height=100px>
<p/>
Comprobamos que la configuración depende del entorno y no del código.

### Logs a stdout: redirige a archivo mediante pipeline de shell y adjunta 5 líneas representativas. Explica por qué no se configura log file en la app.
Corremos la app redirigiendo logs a un archivo:
<p align="center">
    <img src="imagenes/demostracion-parte03.png" width=700px height=100px>
<p/>
En 12-Factor, los logs no se escriben en un archivo propio, sino que se envían a stdout/stderr. Esto permite que el entorno de ejecución (systemd, Docker, Kubernetes, etc.) se encargue de recolectarlos, almacenarlos y procesarlos. Así se logra portabilidad y separación de responsabilidades.

## 5. Operación reproducible (Make/WSL/Linux)
## Empaquetar flujo con Make o script
En el archivo `Respuestas-actividad2.sh` ya tenemos las funciones de Makefile simplificado:

`run:`  levanta la app.

`dns-setup:` agrega miapp.local.

`tls-cert:` genera certificado.

`nginx:` configura reverse proxy.

`tls-checks:` valida handshake.

A continuación tenemos la tabla de comandos:

| Comando                                | Resultado esperado                                     |
|----------------------------------------|--------------------------------------------------------|
| `./Respuestas-actividad2.sh run`         | Flask en `127.0.0.1:8080`, logs en stdout              |
| `curl http://127.0.0.1:8080/`            | JSON con `message` y `release`                         |
| `dig +short miapp.local `                | 127.0.0.1                                              |
| `./Respuestas-actividad2.sh tls-cert`    | Certificado autofirmado en `certs/`                    |
| `./Respuestas-actividad2.sh nginx`       | Nginx escucha en `:443`, proxyea a Flask en `:8080`    |
| `openssl s_client -connect miapp.local:443 -brief` | Handshake TLSv1.2/1.3 exitoso con SNI        |
| `curl -k https://miapp.local/`           | JSON de la app vía HTTPS                               |
| `ss -ltnp` | grep -E ':(443|8080)'       | Evidencia de sockets Flask (8080) y Nginx (443)        |
| `journalctl -u nginx -n 20`              | Logs recientes de Nginx                                |

## Mejora incremental
### Logs estructurados
La aplicación genera logs en formato **JSON por línea** en stodut, lo cual facilitan el parsing porque cada línea ya está en un formato estructurado y estandarizado.:

```json
{"ts": "2025-09-15T17:24:04-0500", "level": "INFO", "event": "startup", "port": 8080}
{"ts": "2025-09-15T17:26:22-0500", "level": "INFO", "event": "request", "method": "GET", "path": "/", "remote": "127.0.0.1", "proto": "http"}
```

### Script end-to-end
Dentro de `Respuestas-actividad2.sh` realizamos el siguiente script.
<p align="center">
    <img src="imagenes/end-to-end.png" width=700px height=300px>
<p/>
Además en la parte de case agregamos dicho script y el comando como será llamado.
Finalmente , lo ejecutamos:
<p align="center">
    <img src="imagenes/end-to-end(2).png" width=700px height=300px>
<p/>

### Preguntas guía
1. HTTP: explica idempotencia de métodos y su impacto en retries/health checks. Da un ejemplo con curl -X PUT vs POST.

- `PUT` es idempotente o también `GET` -> repetirlo no cambia el estado final.
- `POST` no lo es -> cada ejecución puede crear un recurso nuevo.

Ejemplo:

- `curl -X PUT http://127.0.0.1:8080/recurso`
- `curl -X POST http://127.0.0.1:8080/recurso`

2. DNS: ¿por qué hosts es útil para laboratorio pero no para producción? ¿Cómo influye el TTL en latencia y uso de caché?

- **hosts** es útil en laboratorio porque fuerza una resolución rápida, sin depender de un DNS público. En producción no escala, pues requiere modificar manualmente cada máquina.
- El TTL controla cuánto tiempo una respuesta se guarda en caché → afecta latencia y frecuencia de consultas.  
   
3. TLS: ¿qué rol cumple SNI en el handshake y cómo lo demostraste con openssl s_client?
   
El Server Name Indication (SNI) permite al servidor TLS presentar el certificado correcto según el hostname solicitado. Y lo probamos con: 

`openssl s_client -connect miapp.local:443 -servername miapp.local -brief`

4. 12-Factor: ¿por qué logs a stdout y config por entorno simplifican contenedores y CI/CD?
   
- Logs a stdout: simplifican integración con Docker/Kubernetes, permiten recolección centralizada.
- Config por entorno: facilita despliegue en múltiples entornos (dev, staging, prod) sin cambiar código.

5. Operación: ¿qué muestra ss -ltnp que no ves con curl? ¿Cómo triangulas problemas con journalctl/logs de Nginx?
   
`ss -ltnp` muestra sockets y procesos en escucha, lo cual no se ven con `curl` (que solo prueba aplicación).
Triangulación: si `curl` falla, revisas `ss` para confirmar si el puerto está abierto, y `journalctl -u nginx` para verificar errores en el proxy.