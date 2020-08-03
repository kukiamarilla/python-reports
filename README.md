# python-reports

Ejemplo de Generación de Reportes en Python

## Requerimientos

- wkhtmltopdf (https://wkhtmltopdf.org/)
- Python
- Pipenv

## Instalación

Se debe ejecutar el comando `pipenv install` dentro del repositorio, para instalar todas las dependencias necesarias en un nuevo entorno virtual.

Luego, ejecutar `pipenv shell` para entrar dentro del entorno virtual recién creado.

## Uso

El comando `python main.py` generará los reportes con el formato del archivo `report.html` dentro del directorio `output` con los nombre `output.html` y `output.pdf`.

Para modificar el formato del reporte se debe modificar el archivo `report.html`. (se está utilizando la librería de templating `Jinja2`[https://jinja.palletsprojects.com/en/2.11.x/templates/] para el formateo del reporte)

Para modificar los datos con los cuales se van a generar el reporte, calcularlos  en el script `main.py`

