import jinja2
import pandas as pd
import pdfkit

# Se calcula el DataFrame desde el cual se va a generar el reporte (en la variable dataset)
data = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
data = data[data["location"]=="Paraguay"]
data = data.dropna()
dataset = data[["total_cases","date"]]


# Se crea el reporte a partir del contenido de la variable dataset
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "report.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(df=dataset)
html_file = open('./output/out.html', 'w')
html_file.write(outputText)
html_file.close()
pdfkit.from_file("./output/out.html","./output/out.pdf")