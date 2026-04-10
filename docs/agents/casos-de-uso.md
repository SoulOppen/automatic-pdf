# Casos De Uso

## Error Al Generar El PDF

- revisar `lib.py`
- confirmar si Chromium esta instalado
- verificar si `temp.html` se crea
- comprobar rutas de CSS e imagenes
- informar si el problema viene de datos, plantilla, navegador o escritura

Salida esperada: causa probable, evidencia breve, accion o siguiente paso, aprendizaje sobre el pipeline de renderizado.

## Cambio En La Plantilla Del Informe

- revisar `templates/informe.html`
- validar variables Jinja2 contra `lib.py`
- comprobar impacto visual en `static/styles.css`
- advertir si cambia el layout del PDF

Salida esperada: cambio realizado, zonas afectadas, limitacion de verificacion si aplica, aprendizaje sobre plantilla y estilo.

## Problema Con Los Datos Del Excel

- revisar `main.py`
- identificar nombres exactos de columnas
- no normalizar nombres sin acuerdo explicito
- explicar si el problema es de esquema, hoja, ruta o tipo de dato

Salida esperada: columna o condicion que fallo, impacto en informes, propuesta compatible con el esquema actual.

## Actualizacion De Reglas Del Agente

- leer primero la skill `create-rule`
- proponer contenido acorde al repo
- reflejar limites y flujos reales
- evitar plantillas abstractas sin contexto

## Criterios De Calidad

Una buena respuesta:

- usa el vocabulario real del proyecto
- distingue datos fuente, HTML, estilos y PDF
- no exagera el alcance del cambio
- no promete verificaciones no ejecutadas
- deja una conclusion util para el usuario

Una mala respuesta:

- dice solo `listo`
- oculta dependencias reales
- usa skills irrelevantes
- delega sin razon clara
- concluye sin evidencia
