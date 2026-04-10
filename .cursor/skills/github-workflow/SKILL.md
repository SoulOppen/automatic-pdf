---
name: github-workflow
description: Coordina trabajo seguro con GitHub usando git y gh. Use when handling pull requests, branch status, remote checks, PR summaries, GitHub comments, or when the user asks for GitHub-related workflow help.
---

# GitHub Workflow

## Objetivo

Usa esta skill para tareas relacionadas con GitHub, ramas, pull requests y revision de cambios en remoto.

## Cuando Usar

- Revisar o preparar pull requests.
- Resumir cambios para abrir una PR.
- Inspeccionar comentarios, checks o estado remoto.
- Coordinar pasos seguros con `git` y `gh`.

## Limites

- No empujar cambios sin pedido explicito del usuario.
- No usar operaciones destructivas (`reset --hard`, `push --force`, etc.) salvo instruccion clara y consciente.
- No asumir que una PR debe abrirse automaticamente.

## Flujo

1. Confirmar si la tarea es solo de inspeccion o si incluye cambios remotos.
2. Revisar el estado local antes de actuar.
3. Resumir diferencias y contexto de rama.
4. Ejecutar acciones de GitHub solo si el usuario las pidio.
5. Cerrar con estado actual, riesgos y siguientes pasos.

## Reglas

- No hacer `push` sin pedido explicito.
- No usar operaciones destructivas.
- No asumir que debe abrirse una PR automaticamente.
- Si hay cambios locales no relacionados, no revertirlos.
- Si la tarea es solo revisar, priorizar hallazgos y riesgos.

## Salida Recomendada

Usa este formato cuando aplique:

```md
## Estado
[resumen breve]

## Hallazgos
- [punto importante]

## GitHub
- [rama, PR, remoto o siguiente paso]
```

## Casos Tipicos

- revisar si la rama esta lista para PR
- resumir cambios para abrir una PR
- inspeccionar comentarios o checks
- explicar diferencias entre rama local y remota
