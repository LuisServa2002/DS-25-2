# Actividad 05 : Construyendo un pipeline DevOps con Make y Bash
Estudiante : Luis Andre Trujillo Serva
---
## Parte 01 : Construir - Makefile y Bash desde cero
### 1.1 Crear un script Python simple
Iniciamos creando los archivos `__init__.py` y `hello.py` , por último agregamos el `Makefile` proporcionado en la guia.
<p align="center">
    <img src="imagenes/base.png" width=700px height=150px>
<p/>

### 1.2 Crear un Makefile básico
1. Ejecuta `make help` y guarda la salida para análisis. Luego inspecciona `.DEFAULT_GOAL` y `.PHONY` dentro del Makefile. 
   
<p align="center">
    <img src="imagenes/parte01-ejercicio01.png" width=700px height=200px>
<p/>

**Respuesta**

`help` imprime todos los targets que tenemos declarados en nuestro Makefile , además de su respectiva descprición y de acuerdo al comando proporcionado en la guía , este resultado se almacena en `logs/make-help.txt`. Luego , `.DEFAULT_GOAL := help` establece que si se ejecuta `make` sin argumentos , entonces ejecuta por defecto el target de `help` en lugar de intentar compilar algo. Por último , la utilidad de `PHONY` para objetivos como `all`, `clean` o `help` garantiza que siempre se ejecuten, aunque existan archivos con el mismo nombre. De esta forma, se evitan ambigüedades y se asegura un comportamiento consistente.


2. Comprueba la generación e idempotencia de `build`. Limpia salidas previas, ejecuta `build`, verifica el contenido y repite `build` para constatar que no rehace nada si no cambió la fuente.

<p align="center">
    <img src="imagenes/parte01-ejercicio02.png" width=700px height=200px>
<p/>

**Respuesta**

En la primera ejecución de `make build`, se creó la carpeta `out/` y se generó el archivo `out/hello.txt` con la salida del script `src/hello.py`.  
En el segundo comando , Make respondió *“Nothing to be done for 'build'”*, ya que el target estaba actualizado: el archivo fuente no había cambiado y `out/hello.txt` seguía siendo más reciente.  
Esto demuestra la **idempotencia** de `build`: si no se modifica el archivo fuente, el target no se vuelve a generar. El comando `stat` confirmó la misma marca de tiempo, validando que no hubo reconstrucción innecesaria.

3. Fuerza un fallo controlado para observar el modo estricto del shell y `.DELETE_ON_ERROR`. Sobrescribe `PYTHON` con un intérprete inexistente y verifica que no quede artefacto corrupto.

<p align="center">
    <img src="imagenes/parte01-ejercicio03.png" width=700px height=150px>
<p/>

**Respuesta**

Primero eliminamos el archivo `out/hello.txt`. Luego forzamos la ejecución con `PYTHON=python4`, un intérprete inexistente. Make intentó correr , creó el directorio `out/`, pero al no encontrar `python4` se produjo un error y la ejecución se detuvo inmediatamente gracias al **modo estricto** de Bash (`-e -u -o pipefail`).  
La directiva `.DELETE_ON_ERROR` garantizó que el archivo `out/hello.txt` fuera borrado automáticamente, evitando que quedara un artefacto corrupto. Finalmente, al listar el archivo comprobamos que no existe, confirmando que el rollback funcionó correctamente y el sistema mantuvo un estado consistente.

4. Realiza un "ensayo" (dry-run) y una depuración detallada para observar el razonamiento de Make al decidir si rehacer o no. 

<p align="center">
    <img src="imagenes/parte01-ejercicio04.png" width=700px height=400px>
<p/>

**Respuesta**

Con `make -n build` vimos que Make solo nos muestra los comandos que ejecutaría, sin llegar a correrlos.  
Luego, con `make -d build`, Make fue explicando paso a paso cómo analiza: primero revisa el `Makefile`, después verifica si existe `out/hello.txt` y al no encontrarlo decide rehacerlo.  
Se observa en el log frases como *“Must remake target 'out/hello.txt’”* y al final *“Successfully remade target file 'build’”*, lo que confirma que entendió la dependencia y ejecutó las recetas.  


5. Demuestra la incrementalidad con marcas de tiempo. Primero toca la fuente y luego el target para comparar comportamientos.

<p align="center">
    <img src="imagenes/parte01-ejercicio05.png" width=700px height=150px>
<p/>

Cuando modificamos `src/hello.py` con `touch`, Make detectó que el archivo fuente era más reciente que el target y por eso rehizo `out/hello.txt`.  
En cambio, al usar `touch` sobre el propio target (`out/hello.txt`), no se generó nada nuevo: Make entiende que el archivo ya está actualizado porque la fuente no cambió.  
Esto demuestra que la reconstrucción depende de la relación **fuente → target**, no de cambios artificiales en el target.  
De esta forma se garantiza eficiencia: solo se rehace lo necesario y se evita trabajo extra.

6. Ejecuta verificación de estilo/formato manual (sin objetivos `lint/tools`). Si las herramientas están instaladas, muestra sus diagnósticos; si no, deja evidencia de su ausencia.

<p align="center">
    <img src="imagenes/parte01-ejercicio06.png" width=700px height=150px>
<p/>

**Respuesta**

Al ejecutar `shellcheck` y `shfmt` sobre `scripts/run_tests.sh`, los logs mostraron que el archivo no existe en el proyecto actual. Esto significa que no hubo nada que analizar ni formatear, pero los comandos se ejecutaron de forma controlada y los resultados quedaron guardados en `logs/lint-shellcheck.txt` y `logs/format-shfmt.txt`.  
Este ejercicio demuestra que el pipeline está preparado para manejar la ausencia de archivos o herramientas sin romperse, generando siempre evidencia clara de lo ocurrido.

7. Construye un paquete reproducible de forma manual, fijando metadatos para que el hash no cambie entre corridas idénticas. Repite el empaquetado y compara hashes.

<p align="center">
    <img src="imagenes/parte01-ejercicio07.png" width=700px height=300px>
<p/>

**Respuesta**

En este ejercicio generamos y comprimimos el paquete dos veces, obteniendo el mismo hash SHA256 en ambas ejecuciones:  

Esto se logró gracias a las opciones usadas en `tar` y `gzip`:  
- `--sort=name` asegura que los archivos se empaquen siempre en el mismo orden.  
- `--mtime=@0` fija la fecha de modificación a un valor constante.  
- `--owner=0 --group=0 --numeric-owner` establecen usuarios y grupos a valores fijos.  
- `gzip -n` evita que se agreguen nombres de archivo o marcas de tiempo en la compresión.  

De esta forma eliminamos fuentes de variabilidad y garantizamos que el artefacto sea idéntico en cada ejecución, validando la reproducibilidad del build.

8. Reproduce el error clásico "missing separator" sin tocar el Makefile original. Crea una copia, cambia el TAB inicial de una receta por espacios, y confirma el error.

<p align="center">
    <img src="imagenes/parte01-ejercicio08.png" width=700px height=250px>
<p/>

**Respuesta**

Make requiere que todas las líneas de receta comiencen con un **TAB**, no con espacios. Si se usan espacios, aparece el error clásico *“missing separator”*, como se vio en la línea 26 de `Makefile_bad`.  
Este problema es fácil de diagnosticar porque Make indica el número de línea y el mensaje es muy específico. La evidencia del error quedó registrada en `evidencia/missing-separator.txt`, confirmando el comportamiento esperado.

### 1.3 Crear un script Bash
Creamos la carpeta `scripts/` , además el archivo `run_tests.sh` y agregamos su contenido , por último , damos permisos a dicho archivo.
<p align="center">
    <img src="imagenes/parte01-3-creacion.png" width=700px height=150px>
<p/>

##### Ejercicios
- Ejecuta ./scripts/run_tests.sh en un repositorio limpio. Observa las líneas "Demostrando pipefail": primero sin y luego con pipefail. Verifica que imprime "Test pasó" y termina exitosamente con código 0 (`echo $?`).
<p align="center">
    <img src="imagenes/parte01-3-ejercicio01.png" width=700px height=100px>
<p/>

- Edita src/hello.py para que no imprima "Hello, World!". Ejecuta el script: verás "Test falló", moverá hello.py a hello.py.bak, y el trap lo restaurará. Confirma código 2 y ausencia de .bak.

En este caso modificamos el archivo `hello.py`.

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Mundo"))
```
**Resultado**
<p align="center">
    <img src="imagenes/parte01-3-ejercicio02.png" width=700px height=100px>
<p/>

- Ejecuta `bash -x scripts/run_tests.sh` . Revisa el trace: expansión de `tmp` y `PY`, llamadas a funciones, here-doc y tuberías. Observa el trap armado al inicio y ejecutándose al final; estado 0.

<p align="center">
    <img src="imagenes/parte01-3-ejercicio03.png" width=700px height=500px>
<p/>

- Sustituye `output=$("$PY" "$script")` por `("$PY" "$script")`. Ejecuta script. `output` queda indefinida; con `set -u`, al referenciarla en `echo` aborta antes de `grep`. El trap limpia y devuelve código distinto no-cero.

<p align="center">
    <img src="imagenes/parte01-3-ejercicio04(2).png" width=700px height=200px>
<p/>

<p align="center">
    <img src="imagenes/parte01-3-ejercicio04(1).png" width=700px height=150px>
<p/>

El cambio funcionó correctamente: provocó que `output` quedara indefinida, activó el modo estricto (`set -u`), y demostró cómo `trap` asegura limpieza incluso en fallos. El código de salida 2 confirma que se manejó como un fallo de test.

## Parte 2: Leer - Analizar un repositorio completo
### 2.1 Test de ejemplo

## Parte 3: Extender
### 3.1 lint mejorado
### 3.2 Rollback adicional
### 3.3 Incrementalidad
