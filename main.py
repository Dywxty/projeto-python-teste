from flask import Flask 
#Flask =  classe
#flask = biblioteca

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/about")
def about():
    return "<h1>Sobre a página e sua criadora:</h1><p>Esta é uma página simples criada com Flask para um teste em uma aula de python, no curso de Desenvolvimento de Sistemas</p>"

if __name__ == "__main__":
    app.run()