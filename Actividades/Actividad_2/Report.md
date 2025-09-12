# Actividad 02
## 1.HTTP: Fundamentos y herramientas
1. Para **levantar la app** debemos descargar el archivo `Respuestas-actividad2.sh` y antes de ejecutarlo brindar permisos.
<p align="center">
    <img src="imagenes/http-levantar.png" width=450px height=60px>
<p/>
Se ha creado el entorno virtual y luego podemos ejecutar el app.py.
<p align="center">
    <img src="imagenes/http-ejecutar.png" width=450px height=100px>
<p/>

Abrimos una nueva terminal y realizamos el paso siguiente:

2. Inspección con `curl`:
- `curl -v http://127.0.0.1:8080/`
<p align="center">
    <img src="imagenes/http-paso2(1).png" width=450px height=200px>
<p/>

- `curl -i -X POST http://127.0.0.1:8080/` , Visualizamos la respuesta `405 Method Not Allowed` ya que la ruta existe pero no acepta el método **POST** ya que la app solo definio **GET**. Obtendriamos el error `404 Not Found` si la ruta no existiera.
<p align="center">
    <img src="imagenes/http-paso2(2).png" width=450px height=200px>
<p/>

- Respuesta a la pregunta : Nada cambia cuando se encuentra en ejecución , porque `miapp/app.py` lee `APP_MESSAGE` y `APP_RELEASE` desde `os.environ` al iniciar (variables asignadas a variables globales al cargar el módulo). Cambiar las variables de entorno en otra shell no modifica el entorno del proceso que ya está corriendo. Para que una nueva variable afecte a la app hay que reiniciar el proceso (o reimplementar lectura dinámica de configuración).
  
3. Puertos abiertos con `ss`:
   
<p align="center">
    <img src="imagenes/http-paso3.png" width=400px height=80px>
<p/>

`LISTEN` : el estado del socket (esperando conexiones).

`0.0.0.0:8080` : dirección y puerto en el que escucha (todas las interfaces IPv4 en el puerto 8080).

`users:(("python3",pid=12345,fd=3))`: identifica el proceso responsable.

4. Logs como flujo
