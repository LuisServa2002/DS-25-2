# Actividad 3
---
Luis Andre Trujillo Serva
## Parte teórica
1. **Introducción a DevOps: ¿Qué es y qué no es?**
   Explica DevOps desde el código hasta la producción, diferenciándolo de waterfall. Discute "you build it, you run it" en el laboratorio, y separa mitos (ej. solo herramientas) vs realidades (CALMS, feedback, métricas, gates).

DevOps no es solo un conjunto de herramientas, sino una cultura y conjunto de prácticas que integran desarrollo, QA y operaciones para lograr entregas más rápidas y confiables. A diferencia de Waterfall, donde las fases eran rígidas y los errores detectados tarde obligaban a reiniciar procesos completos (generando cuellos de botella), DevOps promueve la colaboración continua bajo la idea de “you build it, you run it”. Esto significa que los equipos que desarrollan también despliegan y operan el software, apoyándose en pipelines de CI/CD, métricas y feedback continuo. Así se reduce la fricción entre áreas y se logra mayor agilidad y calidad en los despliegues.

2. **Marco CALMS en acción:**
   Describe cada pilar y su integración en el laboratorio (ej. Automation con Makefile, Measurement con endpoints de salud). Propón extender Sharing con runbooks/postmortems en equipo.

CALMS es un marco de DevOps que combina principios culturales y técnicos. En el laboratorio se refleja en varios componentes:

**C (Culture):** fomentar una cultura compartida; el Makefile y el Respuestas-actividad2.sh documentan pasos comunes para todos.

**A (Automation):** el Makefile ejecuta tareas repetitivas (crear venv, correr app, generar TLS, configurar Nginx) sin intervención manual.

**L (Lean):** los targets (make run, make all) evitan desperdicio de tiempo y simplifican ciclos de despliegue.

**M (Measurement):** las evidencias (curl, ss, dig) y los endpoints de salud en app.py permiten medir disponibilidad y funcionamiento.

**S (Sharing):** los archivos versionados (REPORT.md, evidencias/) y la propuesta de runbooks/postmortems facilitan compartir conocimiento dentro del equipo.

3. **Visión cultural de DevOps y paso a DevSecOps:**
   Analiza colaboración para evitar silos, y evolución a DevSecOps (integrar seguridad como cabeceras TLS, escaneo dependencias en CI/CD).
   Propón escenario retador: fallo certificado y mitigación cultural. Señala 3 controles de seguridad sin contenedores y su lugar en CI/CD.

4. **Metodología 12-Factor App:**
   Elige 4 factores (incluye config por entorno, port binding, logs como flujos) y explica implementación en laboratorio.
   Reto: manejar la ausencia de estado (statelessness) con servicios de apoyo (backing services).
