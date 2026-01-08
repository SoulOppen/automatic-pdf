# Automatic
---------

Automatic is a Python tool for generating dynamic reports from tabular data. It allows you to combine HTML templates, data processing, and visualizations to produce automated reports in HTML, Excel, and PDF formats.

It is designed to simplify the creation of repetitive reports, eliminating manual work and making template reuse easier.

## Features
--------

*   HTML template rendering using Jinja2
    
*   Data handling and transformation with pandas
    
*   Support for charts generated with matplotlib
    
*   Reading and writing Excel files using openpyxl
    
*   Optional export of reports to PDF using Playwright
    
*   Project management and execution using uv
    

## Motivation
----------

In many projects, report generation involves repetitive tasks: copying data from Excel, manually creating charts, and exporting final documents.

Automatic was created to solve this problem by enabling:

*   Automation of periodic reports
    
*   Consistent design through reusable templates
    
*   Clear separation of data, logic, and presentation
    
*   Reduction of human errors in report generation
    

## Requirements
------------

*   Python 3.12 or higher
    
*   uv installed
    

Install uv:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install uv   `

Main project dependencies:

*   jinja2
    
*   pandas
    
*   matplotlib
    
*   openpyxl
    
*   playwright (optional, only for PDF export)
    

Quick start
-----------

```bash
git clone https://github.com/tu-usuario/automatic.git
cd automatic
```

Install dependencies using uv:
```bash
uv sync
```   

If PDF export will be used, install Playwright browsers:
```bash
uv run playwright install
```

Usage
-----

### Prepare the data

Load and process data using pandas, for example by reading Excel or CSV files.

### Create an HTML template

Define HTML templates using Jinja2 to structure the report.

### Render the report

Combine the processed data with the template to generate the final HTML.

### Export results

*   HTML as direct output
    
*   Excel using openpyxl
    
*   Optional PDF using Playwright
    

## Charts
------

Automatic allows generating charts with matplotlib and integrating them into reports, including:

*   Line charts
    
*   Bar charts
    
*   Pie charts
    
*   Custom visualizations
    

Charts can be exported as images and then referenced from HTML templates.

## Contributing
------------

Contributions are welcome.

Recommended steps:

1.  Fork the project
    
2.  Create a branch for the feature or fix
    
3.  Make changes with clear commits
    
4.  Open a Pull Request
    

## License
-------

This project is distributed under the MIT License.It allows free use, modification, and distribution.

## Project status
--------------

Actively under development.APIs may change while the first version is being stabilized.

Si quieres, también puedo ajustarlo a **estilo README de GitHub**, **documentación técnica**, o **tono más marketing**.

