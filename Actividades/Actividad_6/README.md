# Actividad 6 : Introducción a Git conceptos básicos y operaciones esenciales
Estudiante: Luis Andre Trujillo Serva
---
## Conceptos de Git utilizados
- `git config`: Se logro validar y crear el usuario de nuestro entorno a nivel global para poder trabajar con mis demás repositorios y realizar cada avance mediante los commits.
- `git init`: Cramos un repositorio local , permitiendo llevar un historial de trabajo de nuestra actividad. 
- Mediante `git add` podemos preparar los archivos para luego ser guardados o almacenados , luego , con el comando `git commit` logramos registrar esos cambios. También podemos visualizar que archivos faltan agregar o si ya han sido registrados mediante `git status`. 
- `git log`: Gracias a este comando podemos visualizar las distintas características de un commit , como su hash , el autor , la fecha del registro y el mensaje de dicho commit agregado.
- `Ramas` : Para trabajar con las distintas ramas utilizamos comandos que simplifican dos pasos por ejemplo : `git checkout -b <nombre_rama>` ó `git switch -c <nombre_rama>`.
- `git cherry-pick`: Permite realizar y aplicar un commit especifico a otra rama utilizando su hash , sin necesidad de realizar un merge.
- `git stash`: Permite guardar temporalmente archivos preparados en una rama , además con este comando podemos cambiar de rama sin problemas y para recuperar dichos cambios utilizamos `git stash pop`.
## Preguntas
### git log
- ¿Cual es la salida de este comando : `git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'`?

Mediante dicho comando logramos visualizar el hash reducido del commmit , también cuanto tiempo se realizo dicho commit , el usuario y por último el mensaje registrado del commit.

- Intentemos el comando `git log` en este ejercicio (puedes realizar otra cosa como colocar las cosas en español). Primero, actualiza el archivo `README.md` y crea un nuevo archivo `CONTRIBUTING.md`:

De esta parte podemos resaltar que al realizar una acción mediante `>` esta sobreescribe el archivo que seleccionamos. Por último , mediante `git log --oneline` logramos visualizar los últimos 3 commits realizados.

### Trabajar con ramas

- ¿Cómo te ha ayudado Git a mantener un historial claro y organizado de tus cambios?

Gracias a los commits se puede llevar un historial claro y organizado ya que podremos obtener información del flujo de trabajo de un proyecto , complementado con las ramas los cuales sirven para trabajar de forma paralela.

- ¿Qué beneficios ves en el uso de ramas para desarrollar nuevas características o corregir errores?

EL uso de ramas nos permite trabajar en paralelo sin afectar el programa principal lo cual nos permite trabajar en nuevas funcionalidades y un avance propio.
  
- Realiza una revisión final del historial de commits para asegurarte de que todos los cambios se han registrado correctamente.
  
Gracias a distintos comando como `git log --oneline` podemos visualizar el historial de commits con sus respectivas características y de esta forma verificar lo que se ha registrado. En caso deseemos un gráfico del flujo de estos commits , utilizamos el comando `git log --oneline --graph --all` y además como revisión final.
  
- Revisa el uso de ramas y merges para ver cómo Git maneja múltiples líneas de desarrollo.

Gracias al uso de `git merge` podemos integrar los archivos y los historiales de una rama a otra , además en caso de conflictos , se detiene en el proceso para que este sea resuelto de manera manual.

## Ejercicios
#### Ejercicio 1: Manejo avanzado de ramas y resolución de conflictos
Los resultados de este ejercicio se almacenaron en `merge-o-conflicto.txt`

#### Ejercicio 2: Exploración y manipulación del historial de commits
- Mediante `git log -p` visualizamos los commits más especificos , además logramos visualizar que se ha agregado y eliminado.
- En el caso de revertir el commit , este último era cuando realizamos el merge por lo cual habrá conflictos , por lo tanto usamos `git revert -m 1 HEAD`.
  
Bueno en mi caso como seguimos trabajando en la rama main y en pasos anteriores se eliminaron ramas especificas , entonces se visualiza un gráfico de una sola línea ya que seguimos trabajando en main , pero sí se logro realizar el rebase de 3 commits en uno solo.

- Después del revert:
```
ef7fe9a (HEAD -> main) Revert "Resuelve el conflicto de fusión entre la versión main y feature/advanced-feature"
21846c7 Resuelve el conflicto de fusión entre la versión main y feature/advanced-feature
7f3be48 Actualizar el mensaje main.py en la rama main
45b9489 Agrega la funcion greet como funcion avanzada
6d3ab1b (rama_hash, rama_especifica) Agrega main.py
d1255ce Configura la documentación base del repositorio
595e4f7 Commit inicial con README.md
```

- Después del rebase:
```
* 89bf6f3 (HEAD -> main) Fusiona cambios en main.py
* 6d3ab1b (rama_hash, rama_especifica) Agrega main.py
* d1255ce Configura la documentación base del repositorio
* 595e4f7 Commit inicial con README.md
```

#### Ejercicio 3: Creación y gestión de ramas desde commits específicos
Se logro crear la rama con el último hash y además se modifico el `main.py` , luego se realizo un merge y por último se elimino la rama `bugfix/rollback-feature`.

#### Ejercicio 4: Manipulación y restauración de commits con git reset y git restore
Para ambos ejercicios se logro lo planteado en la guía , almacenando el resultado en `logs/reset` y `logs/restore`.

#### Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests
Para este proceso cree otro repositorio y además lo clone en otra carpeta , el resultado se almacena en `pull.txt`.

#### Ejercicio 6: Cherry-Picking y Git Stash
Se logro agregar el commit de main a la rama feature/cherry-pick mediante el comando `git cherry-pick <hash>` y mediante `git stash` logramos guardar temporalmente algunos cambios realizados , como comentario extra , si agregamos algun archivo pero no realizamos el commit y queremos cambiar de rama , obtendremos un error , pero mediante el comando de `git stash` podemos evitar este problema.