import os
from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright
def gen_pdf(
    name:str,
    account:str,
    info_persona:list[str],
    original_account_value:float,
    incomes:float,
    charge:float,
    end_account_value:float,
    value_with_accrued:float,
    annual_income:float,
    tipos:list[tuple[int,str]]
    ):
    print("Iniciando Creacion de Pdf")
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('./templates/informe.html')
    data = {
        "name_advisor":name,
        "persona":info_persona,
        "account":account,
        "original_account_value":original_account_value,
        "incomes":incomes,
        "charge":charge,
        "end_account_value":end_account_value,
        "value_with_accrued":value_with_accrued,
        "annual_income":annual_income,
        "tipos":tipos
    }
    static_path = os.path.abspath("static/styles.css")
    html_content = template.render(data)
    html_content = html_content.replace("../static/styles.css", f"file:///{static_path}")
    img_path = os.path.abspath("templates/src/img.png")
    html_content = html_content.replace("./src/img.png", f"file:///{img_path}")
    temp_path = "temp.html"
    os.makedirs("informes", exist_ok=True)
    path=os.path.join("informes",f"{account}.pdf")
    if os.path.exists(path):
        os.remove(path)

    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()


        page.goto("file://" + os.path.abspath(temp_path))


        page.wait_for_load_state("networkidle")

        page.pdf(
            path=path,
            format="A4",
            margin={"top": "15mm", "bottom": "15mm", "left": "10mm", "right": "10mm"},
            print_background=True
        )

        browser.close()
    os.remove(temp_path)
    print(f"✅ PDF generado correctamente: {path}")