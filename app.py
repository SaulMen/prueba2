from flask import Flask, request
from flask_cors import CORS
from usuario import usuario
from datetime import datetime as dt
from userController import userController

usuario_obj = usuario(1, "saul","saumen","123",0)
mis_usuario = userController()


app =  Flask(__name__)
CORS(app)

@app.route('/')
def index():
	return "<h1>Bienvenido</h1>"

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

@app.route("/usuario_crear", methods=['GET', 'POST', 'PUT', 'DELETE'])
def usuario_crear():

    response = {}

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        user_name = request.form.get('user_name')
        user_pass = request.form.get('user_pass')
        rol = request.form.get('rol')

        if (mis_usuario.crear(nombre, user_name, user_pass, rol)):
            response['status'] = 100
            response['info'] = "usuario creado correctamente"
        else:
            response['status'] = 300
            response['info'] = 'No se pudo realizar la acción'
    
    elif request.method == 'GET':
        id = int(request.args.get("id", None))
    
        return mis_usuario.devolver_usuario(id)

    elif request.method == 'DELETE':
        id = int(request.args.get("id", None))
        if mis_usuario.eliminar(id):
            response['status'] = 200
            response['info'] = "Usuario eliminado correctamente" 
        else: 
            response['status'] = 300
            response['info'] = 'No se pudo realizar la acción'

    return response    
   #print(rol + user_name + user_pass + nombre)

if __name__=="__main__":
    app.run(threaded=True, port=5001, debug=True)    

