# Subagentes

## Proposito

Documentacion de cuando delegar y que esperar de cada tipo de subagente. El agente principal consulta esto para decidir si conviene exploracion, comandos o sintesis amplia.

## Regla Base

Los subagentes reparten trabajo especializado, pero la sintesis final, la decision final y la respuesta al usuario siempre pertenecen al agente principal.

## Cuando Resolver Directo

Resolver sin subagentes cuando la tarea sea:

- lectura o edicion de uno o pocos archivos conocidos
- ajuste puntual en `main.py`, `lib.py`, `templates/informe.html` o `static/styles.css`
- explicacion simple del pipeline `Excel -> HTML -> PDF`
- cambio pequeno de texto o documentacion
- validacion corta que no requiera exploracion amplia

## Cuando Delegar

Delegar cuando la tarea tenga varias etapas, varias zonas del repo o necesite comparacion, verificacion o exploracion amplia.

## Subagente `explore`

### Cuando Usarlo

- mapear el repo cuando la duda es amplia
- localizar rapidamente donde se define un comportamiento
- buscar dependencias entre Excel, plantilla, estilos y PDF
- investigar varias areas en paralelo

### Cuando Evitarlo

- cuando ya se conoce el archivo exacto
- cuando una lectura directa es suficiente

### Resultado Esperado

Rutas concretas, hallazgos accionables y un resumen que el agente principal pueda sintetizar sin releer todo.

## Subagente `shell`

### Cuando Usarlo

- ejecutar comandos de `git`
- correr comandos de `uv`
- lanzar verificaciones con Python o Playwright
- inspeccionar errores de ejecucion o artefactos generados

### Cuando Evitarlo

- cuando el objetivo es leer archivos ya conocidos
- cuando existe una herramienta mas especifica para lectura o busqueda

### Resultado Esperado

Evidencia de ejecucion, errores relevantes y una interpretacion breve para explicar el estado al usuario.

## Subagente `generalPurpose`

### Cuando Usarlo

- tareas multi paso con investigacion, sintesis y propuesta
- redaccion de documentacion amplia basada en varios archivos
- comparacion de alternativas de implementacion
- explicaciones tecnicas extensas

### Cuando Evitarlo

- cuando una lectura directa o una edicion puntual basta
- cuando la tarea depende sobre todo de ejecutar comandos

### Resultado Esperado

Sintesis estructurada y util para integrar en una respuesta final clara.
