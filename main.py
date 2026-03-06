from flask import Flask 
#Flask =  classe
#flask = biblioteca

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()