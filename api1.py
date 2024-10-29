from flask import Flask
app = Flask(__name__)
@app.route("/") # decorador para ruta raíz
def hello_world():
    print("Hello World")
