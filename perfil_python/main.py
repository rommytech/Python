from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #Ruta principal
def hello():
    nombre_autor = "Rommy"
    data_para_html = { #Diccionario
        "autor": nombre_autor,
        "titulo": "Data science",
        "tecnologias": ["Python", "Ruby", "Elixir"]
    }

    return render_template("index.html", data = data_para_html)

if __name__ == "__main__": #Estamos en el archivo principal
        app.run(debug=True)

