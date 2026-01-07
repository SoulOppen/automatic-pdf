# AUTOMATIC

Automatic es una herramienta en Python para la generación de reportes dinámicos a partir de datos tabulares. Permite combinar plantillas HTML, procesamiento de datos y visualizaciones para producir reportes en HTML, Excel y PDF de forma automatizada.

Está pensada para simplificar la creación de reportes repetitivos, eliminando trabajo manual y facilitando la reutilización de plantillas.

## CARACTERÍSTICAS

*   Renderizado de plantillas HTML usando Jinja2
    
*   Manejo y transformación de datos con pandas
    
*   Soporte para gráficos generados con matplotlib
    
*   Lectura y escritura de archivos Excel mediante openpyxl
    
*   Exportación opcional de reportes a PDF usando Playwright
    
*   Gestión y ejecución del proyecto utilizando uv
    

## MOTIVACIÓN

En muchos proyectos, la generación de reportes implica tareas repetitivas: copiar datos desde Excel, crear gráficos manualmente y exportar documentos finales.

Automatic nace para resolver ese problema, permitiendo:

*   Automatizar reportes periódicos
    
*   Mantener un diseño consistente mediante plantillas
    
*   Separar datos, lógica y presentación
    
*   Reducir errores humanos en la generación de informes
    

## REQUISITOS

*   Python 3.12 o superior
    
*   uv instalado
    

Instalación de uv:

pip install uv

Dependencias principales del proyecto:

*   jinja2
    
*   pandas
    
*   matplotlib
    
*   openpyxl
    
*   playwright (opcional, solo para exportar a PDF)
    

## QUICK START

Clonar el repositorio:

git clone https://github.com/tu-usuario/automatic.gitcd automatic

Instalar dependencias usando uv:

uv sync

Si se usará exportación a PDF, instalar los navegadores de Playwright:

uv run playwright install

## USO

1.  Preparar los datos
    

Cargar y procesar datos usando pandas, por ejemplo leyendo archivos Excel o CSV.

1.  Crear una plantilla HTML
    

Definir plantillas HTML utilizando Jinja2 para estructurar el reporte.

1.  Renderizar el reporte
    

Combinar los datos procesados con la plantilla para generar el HTML final.

1.  Exportar resultados
    

*   HTML como salida directa
    
*   Excel mediante openpyxl
    
*   PDF de forma opcional usando Playwright
    

GRÁFICOS

Automatic permite generar gráficos con matplotlib e integrarlos dentro de los reportes, incluyendo:

*   Gráficos de líneas
    
*   Gráficos de barras
    
*   Gráficos de torta
    
*   Visualizaciones personalizadas
    

Los gráficos pueden exportarse como imágenes y luego ser referenciados desde las plantillas HTML.

## CONTRIBUIR

Las contribuciones son bienvenidas.

Pasos recomendados:

1.  Hacer un fork del proyecto
    
2.  Crear una rama para la funcionalidad o corrección
    
3.  Realizar los cambios con commits claros
    
4.  Abrir un Pull Request
    

LICENCIA

Este proyecto se distribuye bajo la licencia MIT.Se permite su uso, modificación y distribución libremente.

ESTADO DEL PROYECTO

En desarrollo activo.Las APIs pueden cambiar mientras se estabiliza la primera versión.

