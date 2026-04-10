---
name: test-workflow
description: Planifica y ejecuta verificacion proporcional al cambio. Use when running tests, choosing what to validate, checking build or runtime behavior, or when the user asks to verify that something works.
---

# Test Workflow

## Objetivo

Usa esta skill para decidir como verificar cambios sin sobredimensionar la validacion.

## Cuando Usar

- Ejecutar pruebas o checks que el repo ya provea.
- Diseñar verificacion proporcional al cambio.
- Explicar que no pudo verificarse y por que.
- Priorizar pruebas o validaciones de mayor valor.

## Limites

- No inventar suites de prueba que el repositorio no tenga configuradas.
- No ejecutar validaciones costosas si no aportan valor al cambio concreto.
- No afirmar cobertura o exito sin evidencia real (salida de comando, archivo generado, etc.).

## Flujo

1. Identificar que cambio se hizo.
2. Elegir la verificacion de mayor valor y menor costo razonable.
3. Ejecutar pruebas, checks o validaciones manuales relevantes.
4. Registrar que se verifico y que no pudo verificarse.
5. Cerrar con riesgos residuales.

## Reglas Adicionales

- Si falta un prerequisito (Excel local, Chromium, etc.), decirlo explicitamente en la respuesta al usuario.
- Las reglas de verificacion por archivo de este repositorio estan solo en `docs/agents/verificacion.md`; no duplicar esa lista aqui.

## Salida Recomendada

```md
## Verificacion
- Ejecutado: [check real]
- No ejecutado: [motivo real]

## Riesgos
- [riesgo residual]
```
