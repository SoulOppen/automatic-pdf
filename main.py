import pandas as pd
import matplotlib.pyplot as plt

from lib import gen_pdf
def main():
    df_data = pd.read_excel(
    "static/excel.xlsx",
    sheet_name="Hoja2",
)
    porcentajes=[25,25,45,5]
    nombres=["Bimini","Wynwood","Atlantic isles","Cash"]
    plt.pie(porcentajes, labels=nombres)
    plt.title("Distribución de Assets")
    plt.savefig("templates/src/img.png")
    for i in range(len(df_data)):
        fila = df_data.iloc[i]
        gen_pdf(
            name=fila["Financial advisor"],
            account=fila["Accoiunt number"],
            info_persona=[fila["Cliente Name"]],
            original_account_value=fila["Beginning account value"],
            incomes=fila["Dividens, interés, and other income"],
            charge=fila["Administration Charge"],
            end_account_value=fila["Ending account value"],
            value_with_accrued=fila["Account  value with accruerd interest"],
            annual_income=fila["Estimate annual income"],
            tipos=list(zip(porcentajes,nombres))
        )
if __name__=="__main__":
    main()