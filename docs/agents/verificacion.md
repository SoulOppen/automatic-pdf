# Verificacion

## Reglas Por Archivo

Segun el tipo de cambio, verificar de forma proporcional:

- Si cambia `main.py`, validar lectura del Excel, grafico y llamada a `gen_pdf`.
- Si cambia `lib.py`, validar rutas absolutas, HTML temporal y exportacion PDF.
- Si cambia `templates/informe.html`, revisar placeholders Jinja2 y rutas de assets.
- Si cambia `static/styles.css`, verificar compatibilidad visual con impresion y PDF.
- Si cambia documentacion, revisar coherencia con el flujo real del repo.

## Prerequisitos

Si no se puede verificar por falta de `excel.xlsx`, ausencia de Chromium para Playwright o cualquier otro prerequisito, decirlo explicitamente.

## Comandos Frecuentes

```powershell
uv sync
uv run playwright install chromium
uv run python main.py
```

Si la tarea no requiere ejecutar el pipeline completo, no hacerlo por inercia.

## Skill Relacionada

Para criterios de verificacion reutilizables en el agente, ver tambien `.cursor/skills/test-workflow/SKILL.md`.
