import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
def main():
    print("Hola")
    c = canvas.Canvas("ejemplo.pdf")

    # Escribir texto
    c.drawString(100, 750, "Hola, este es mi primer PDF con ReportLab")

    # Guardar el archivo
    c.save()
if __name__=="__main__":
    main()