from pathlib import Path
from typing import Sequence

from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
TEMPLATE_PATH = "templates/informe.html"
STATIC_CSS = ROOT / "static" / "styles.css"
IMG_PATH = ROOT / "templates" / "src" / "img.png"
INFORMES_DIR = ROOT / "informes"


def gen_pdf(
    name: str,
    account: str,
    info_persona: list[str],
    original_account_value: float,
    incomes: float,
    charge: float,
    end_account_value: float,
    value_with_accrued: float,
    annual_income: float,
    tipos: Sequence[tuple[int, str]],
) -> Path:
    """Renderiza la plantilla y exporta un PDF en `informes/{account}.pdf`."""
    print("Iniciando Creacion de Pdf")
    env = Environment(loader=FileSystemLoader(str(ROOT)))
    template = env.get_template(TEMPLATE_PATH)
    data = {
        "name_advisor": name,
        "personas": info_persona,
        "account": account,
        "original_account_value": original_account_value,
        "incomes": incomes,
        "charge": charge,
        "end_account_value": end_account_value,
        "value_with_accrued": value_with_accrued,
        "annual_income": annual_income,
        "tipos": list(tipos),
    }
    css_uri = STATIC_CSS.resolve().as_uri()
    img_uri = IMG_PATH.resolve().as_uri()
    html_content = template.render(data)
    html_content = html_content.replace("../static/styles.css", css_uri)
    html_content = html_content.replace("./src/img.png", img_uri)

    INFORMES_DIR.mkdir(parents=True, exist_ok=True)
    pdf_path = INFORMES_DIR / f"{account}.pdf"
    if pdf_path.exists():
        pdf_path.unlink()

    temp_path = ROOT / "temp.html"
    try:
        temp_path.write_text(html_content, encoding="utf-8")
        html_uri = temp_path.resolve().as_uri()
        with sync_playwright() as p:
            browser = p.chromium.launch()
            try:
                page = browser.new_page()
                page.goto(html_uri)
                page.wait_for_load_state("networkidle")
                page.pdf(
                    path=str(pdf_path),
                    format="A4",
                    margin={
                        "top": "15mm",
                        "bottom": "15mm",
                        "left": "10mm",
                        "right": "10mm",
                    },
                    print_background=True,
                )
            finally:
                browser.close()
    finally:
        if temp_path.exists():
            temp_path.unlink()

    print(f"✅ PDF generado correctamente: {pdf_path}")
    return pdf_path
