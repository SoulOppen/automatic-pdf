# AGENTS.md

## Proposito

Puerta de entrada del agente orquestador de este repositorio. Las reglas operativas detalladas y el contexto del proyecto viven en `docs/agents/`; las skills reutilizables en `.cursor/skills/`.

El agente debe:

- entender el flujo real del proyecto (ver [contexto-del-repo.md](docs/agents/contexto-del-repo.md))
- elegir entre resolver directo o delegar (ver [subagentes.md](docs/agents/subagentes.md))
- usar skills solo cuando aporten valor
- seguir el protocolo de respuesta y aprendizajes visibles (ver [protocolo-de-respuesta.md](docs/agents/protocolo-de-respuesta.md))

## Decision Operativa

- Resolver directo si la tarea afecta pocos archivos conocidos o requiere una explicacion simple.
- Delegar a subagentes si hay varias zonas del repo, exploracion amplia o verificacion multi paso.
- Mantener siempre la sintesis y la decision final en el agente principal.
- Cerrar tareas sustantivas con `Aprendizajes` o `Hallazgos`.

## Mapa De Documentos

| Documento | Contenido |
|-----------|-----------|
| [docs/agents/contexto-del-repo.md](docs/agents/contexto-del-repo.md) | Flujo del pipeline, restricciones, dependencias y riesgos (fuente unica para eso). |
| [docs/agents/subagentes.md](docs/agents/subagentes.md) | Cuando delegar, subagentes `explore`, `shell`, `generalPurpose`. |
| [docs/agents/protocolo-de-respuesta.md](docs/agents/protocolo-de-respuesta.md) | Secuencia de trabajo, progreso en pantalla, formato de salida. |
| [docs/agents/verificacion.md](docs/agents/verificacion.md) | Reglas de verificacion por archivo, comandos, prerequisitos. |
| [docs/agents/casos-de-uso.md](docs/agents/casos-de-uso.md) | Casos concretos del repo y criterios de calidad de respuesta. |
| [.cursor/skills/github-workflow/SKILL.md](.cursor/skills/github-workflow/SKILL.md) | Skill de flujo GitHub (`git`, `gh`, PRs). |
| [.cursor/skills/test-workflow/SKILL.md](.cursor/skills/test-workflow/SKILL.md) | Skill de verificacion y pruebas proporcionales. |

## Regla Final

El agente debe ser mas util que verboso. Cada tarea debe dejar un resultado claro y una mejor comprension del flujo descrito en `contexto-del-repo.md`.
