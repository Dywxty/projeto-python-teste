from flask import Flask 
#Flask =  classe
#flask = biblioteca

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/curso")
def curso():
    return "<h1>Curso:</h1><br><p>Desenvolvimento de Sistemas</p>"

if __name__ == "__main__":
    app.run()