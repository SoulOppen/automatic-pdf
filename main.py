from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from lib import gen_pdf

EXCEL_PATH = "static/excel.xlsx"
SHEET_NAME = "Hoja2"
CHART_PATH = Path("templates/src/img.png")

ASSET_PERCENTAGES = [25, 25, 45, 5]
ASSET_NAMES = ["Bimini", "Wynwood", "Atlantic isles", "Cash"]


def write_asset_pie_chart() -> None:
    CHART_PATH.parent.mkdir(parents=True, exist_ok=True)
    plt.pie(ASSET_PERCENTAGES, labels=ASSET_NAMES)
    plt.title("Distribución de Assets")
    plt.savefig(CHART_PATH)
    plt.close()


def load_accounts_dataframe() -> pd.DataFrame:
    return pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)


def row_to_gen_pdf_kwargs(row: pd.Series, tipos: list[tuple[int, str]]) -> dict:
    """Mapea una fila del Excel a los argumentos de gen_pdf (nombres de columna sin cambiar)."""
    return {
        "name": row["Financial advisor"],
        "account": row["Accoiunt number"],
        "info_persona": [row["Cliente Name"]],
        "original_account_value": row["Beginning account value"],
        "incomes": row["Dividens, interés, and other income"],
        "charge": row["Administration Charge"],
        "end_account_value": row["Ending account value"],
        "value_with_accrued": row["Account  value with accruerd interest"],
        "annual_income": row["Estimate annual income"],
        "tipos": tipos,
    }


def main() -> None:
    write_asset_pie_chart()
    df_data = load_accounts_dataframe()
    tipos = list(zip(ASSET_PERCENTAGES, ASSET_NAMES))
    for _, row in df_data.iterrows():
        gen_pdf(**row_to_gen_pdf_kwargs(row, tipos))


if __name__ == "__main__":
    main()
