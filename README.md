<div align="center">

![Banner del proyecto](docs/assets/readme-banner.svg)

[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-sync-5A2FC7?style=for-the-badge&logo=uv&logoColor=white)](https://github.com/astral-sh/uv)
[![Playwright](https://img.shields.io/badge/Playwright-Chromium-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![Jinja2](https://img.shields.io/badge/Jinja2-plantillas-B41717?style=for-the-badge&logo=jinja&logoColor=white)](https://jinja.palletsprojects.com/)
[![pandas](https://img.shields.io/badge/pandas-datos-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

[![Repo](https://img.shields.io/badge/GitHub-automatic--pdf-181717?style=flat-square&logo=github)](https://github.com/SoulOppen/automatic-pdf)
[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-yellow?style=flat-square)](https://opensource.org/licenses/MIT)

</div>

---

## ¿Qué es?

**Automatic PDF** es una herramienta en Python que genera **informes en PDF** a partir de datos en **Excel**, una plantilla **HTML** con **Jinja2**, estilos **CSS** y exportación con **Playwright** (Chromium).

Flujo resumido:

```text
static/excel.xlsx  →  pandas + matplotlib  →  templates/informe.html  →  informes/*.pdf
```

## Vista previa del flujo

![Diagrama del flujo de datos](docs/assets/readme-flujo.svg)

## Características

- Plantillas HTML con **Jinja2**
- Datos y transformaciones con **pandas**
- Gráficos con **matplotlib** (integrados en el informe)
- Lectura de Excel con **openpyxl**
- PDF con **Playwright** (Chromium)
- Entorno y dependencias con **uv**

## Requisitos

- Python **3.12 o superior**
- [**uv**](https://github.com/astral-sh/uv) instalado:

```bash
pip install uv
```

## Inicio rápido

```bash
git clone https://github.com/SoulOppen/automatic-pdf.git
cd automatic-pdf
uv sync
```

Para generar PDFs necesitas los navegadores de Playwright:

```bash
uv run playwright install chromium
```

Coloca tu archivo **`static/excel.xlsx`** (no se versiona por defecto; está en `.gitignore`) con la hoja y columnas que espera el código, y ejecuta:

```bash
uv run python main.py
```

Los PDFs se escriben en la carpeta **`informes/`**.

## Estructura relevante

| Ruta | Rol |
|------|-----|
| `main.py` | Lee Excel, genera el gráfico y llama a la generación por fila |
| `lib.py` | Renderiza la plantilla y exporta el PDF con Playwright |
| `templates/informe.html` | Plantilla del informe |
| `static/styles.css` | Estilos del HTML impreso a PDF |

## Agente y documentación para IA

Si usas asistentes de código en el repo, consulta [`AGENTS.md`](AGENTS.md) y la carpeta [`docs/agents/`](docs/agents/).

## Contribuciones

1. Fork del repositorio  
2. Rama para la funcionalidad o corrección  
3. Commits claros  
4. Pull Request hacia `main`

## Licencia

Este proyecto se distribuye bajo la **licencia MIT** (si aún no hay archivo `LICENSE` en la raíz, conviene añadirlo para formalizar los términos).

## Estado del proyecto

En desarrollo activo; la API interna puede cambiar mientras se estabiliza la primera versión usable en producción.
