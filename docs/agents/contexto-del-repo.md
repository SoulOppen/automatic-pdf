# Contexto Del Repo

## Objetivo

Este repositorio genera informes PDF a partir de datos en Excel, una plantilla HTML renderizada con Jinja2, estilos CSS y una exportacion final con Playwright.

## Flujo Real

- `main.py` lee `static/excel.xlsx`.
- `main.py` genera un grafico con `matplotlib` en `templates/src/img.png`.
- `main.py` llama a `gen_pdf(...)` definido en `lib.py`.
- `lib.py` renderiza `templates/informe.html`.
- `lib.py` reescribe rutas relativas a `file:///` para CSS e imagenes.
- `lib.py` genera `temp.html` como archivo transitorio.
- `lib.py` exporta el PDF final dentro de `informes/`.

## Archivos Clave

- `main.py`
- `lib.py`
- `templates/informe.html`
- `static/styles.css`
- `pyproject.toml`
- `README.md`

## Restricciones Reales

- Ejecutar siempre desde la raiz del repo.
- No asumir que `static/excel.xlsx` existe en git, porque `*.xlsx` esta ignorado.
- No commitear PDFs ni contenido de `informes/`.
- Tratar `temp.html` como artefacto temporal.
- Recordar que `templates/src/img.png` se genera durante la ejecucion.
- No renombrar columnas del Excel sin revisar el flujo completo.
- Tener presente que Playwright necesita Chromium instalado.

## Dependencias Tecnicas

- Python `>=3.12`
- `jinja2`
- `matplotlib`
- `openpyxl`
- `pandas`
- `playwright`

## Riesgos Tipicos

- fallo por columnas mal escritas o no coincidentes en el Excel
- ausencia del navegador de Playwright
- rutas relativas rotas entre HTML, CSS e imagen
- cambios visuales en la plantilla que alteran el layout del PDF
