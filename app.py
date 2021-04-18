from datetime import datetime as dt
from flask import Flask
from flask_cors import CORS
from models.usuario import usuario

usuario_obj = usuario(1, "saul","123")

app =  Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "<h1>Bienvenidos</h1>"

@app.route("/saludar")
def saludar():
    return "<h1>Hola como estas</h1>"

@app.route("/datetime")
def datetime():
    now_utc = dt.now()
    return "<h1>"+str(now_utc)+"</h1>"

@app.route("/user")
def user():
    return "<h1>"+usuario_obj.user_name+" es el admom</h1>"

if __name__=="__main__":
    app.run(threaded=True, port=5001, debug=True)    

