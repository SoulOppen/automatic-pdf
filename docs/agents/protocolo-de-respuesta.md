# Protocolo De Respuesta

## Secuencia De Trabajo

Para cada pedido, el agente debe:

1. Confirmar el objetivo en una frase.
2. Reunir el contexto minimo necesario.
3. Decidir si resuelve directo o con subagentes.
4. Informar brevemente que va a revisar o cambiar.
5. Ejecutar el trabajo.
6. Verificar en proporcion al cambio (ver [verificacion.md](verificacion.md)).
7. Entregar una respuesta final clara.
8. Cerrar con `Aprendizajes`, `Hallazgos` o riesgos residuales.

## Protocolo De Respuesta En Pantalla

Las actualizaciones de progreso deben indicar, de forma breve:

- que esta entendiendo
- que parte del repo esta inspeccionando
- que editara a continuacion
- que validacion esta ejecutando

## Formato Recomendado De Salida

Para tareas de investigacion, implementacion o depuracion, tender a esta estructura:

### Resultado

Sintesis corta del objetivo resuelto.

### Cambios O Hallazgos

Resumen de los puntos tecnicos realmente importantes.

### Verificacion

Que se ejecuto, que se observo o que no pudo verificarse.

### Aprendizajes

Entre 2 y 5 puntos concretos y reutilizables para el usuario.

Si la tarea es muy simple, puede compactar esta estructura en un solo bloque, sin perder claridad.
