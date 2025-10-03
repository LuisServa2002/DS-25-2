# Actividad 07: Explorando estrategias de fusión en Git
Estudiante : Luis Andre Trujillo Serva
## Ejercicios
### A. Evitar (o no) --ff
Pregunta: ¿Cuándo evitarías --ff en un equipo y por qué?

Cuando necesito preservar la trazabilidad de la integración (saber cuándo y por qué se fusionó una rama).
El fast-forward “aplana” la rama como si nunca hubiera existido, lo cual es ideal en proyectos individuales, pero en equipos puede ocultar la historia de colaboración.

### B. Trabajo en equipo con --no-ff
Preguntas: ¿Qué ventajas de trazabilidad aporta? ¿Qué problemas surgen con exceso de merges?

- **Ventajas de trazabilidad**: Se conserva el merge commit, lo que muestra claramente en el DAG cuándo se integró una rama. Esto ayuda en auditorías y revisiones de PR.

- **Problemas con exceso de merges**: Si el equipo crea merges para cada cambio trivial, el historial se llena de commits de fusión innecesarios y se vuelve difícil de leer.

### C. Squash con muchos commits
Preguntas: ¿Cuándo conviene? ¿Qué se pierde respecto a merges estándar?

Conviene cuando quiero mantener la rama main muy limpia, con un solo commit representativo por feature, aunque internamente la rama tuviera 10 commits de prueba. Pero se pierde el detalle del trabajo interno de la rama (no queda el DAG enlazado, no aparece el historial de cada commit intermedio).

### Conflictos reales con no-fast-forward
#### Preguntas
- ¿Qué pasos adicionales hiciste para resolverlo?
  
Al realizar el merge de tipo no-fast-forward tuve un conflicto ya que ambos `ìndex.html` tenían un contenido diferente en la primera linea , esto se soluciono de manera manual cuando eliminamos las marcas para al final fusionarlo.

- ¿Qué prácticas (convenciones, PRs pequeñas, tests) lo evitarían?
    - Convenciones de estilo de código comunes.
    - Pull Requests pequeños y frecuentes.
    - Pruebas automatizadas que verifiquen la integración.
    - Comunicación clara en el equipo sobre qué archivos se están modificando.

### Comparar historiales tras cada método
#### Preguntas
- ¿Cómo se ve el DAG en cada caso?
  
Por ejemplo en `05-compare-fastforward.log` visualizamos un historial lineal , los asteriscos (*) representan el flujo principal (main) y las ramas laterales aparecen pero se integran como si fueran parte de la línea recta. 

En `06-compare-noff.log` se muestra los commits de tipo merge, aquí aparecen claramente los commits que integran ramas con --no-ff.

Por último en `07-compare-squash.log` muestra todo el flujo de los commits , aunque `main` solo guarda un commit de squash, en el DAG aparecen los commits internos de `feature-3`.

- ¿Qué método prefieres para: trabajo individual, equipo grande, repos con auditoría estricta?

    - **Trabajo individual**:
Prefiero fast-forward (--ff), porque me da un historial limpio y lineal.
    - **Equipo grande**:
Prefiero no-fast-forward (--no-ff), ya que los merge commits permiten identificar claramente cuándo se integró una rama y quién la hizo.

    - **Repos con auditoría estricta (CI/CD, DevSecOps)**:
Prefiero no-ff o incluso merge firmado , porque la trazabilidad de la integración y la validez de la autoría son más importantes que la limpieza del historial.

### Revertir una fusión (solo si HEAD es un merge commit)
#### Preguntas
- ¿Cuándo usar git revert en vez de git reset?
  
`git revert` se usa cuando quiero deshacer un cambio sin borrar el historial, generando un nuevo commit que “revierte” lo anterior.
Es ideal en repositorios compartidos, porque mantiene la trazabilidad y no rompe el historial de otros colaboradores.
En cambio , `git reset` reescribe el historial (mueve punteros), y eso puede causar problemas graves si ya compartiste esos commits en remoto.    

- ¿Impacto en un repo compartido con historial público?
  
Si uso git revert, el historial sigue intacto y todos los colaboradores pueden sincronizar sin conflictos.
Si uso git reset en un repo compartido, el historial diverge y los demás tendrán errores al hacer pull/push (se requiere --force, lo cual puede sobrescribir el trabajo de otros).
Por eso en un repo público/colaborativo, lo seguro es usar git revert.

### Variantes útiles para DevOps/DevSecOps
#### F. Sesgos de resolución y normalización (algoritmo ORT)

Para probar conflictos usé la opción -X ours, que me permitió quedarme con los cambios de la rama main y descartar lo de la rama secundaria. Esto es útil cuando quiero priorizar la versión estable del proyecto sin tener que resolver línea por línea. La alternativa -X theirs hace lo contrario (se queda con los cambios de la rama que se está fusionando).
