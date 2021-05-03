from flask import Flask, request
from flask_cors import CORS
from usuario import usuario
from datetime import datetime as dt
from userController import userController
from doctor import doctor
from doctorController import doctorController
from enfermeraController import enfermeraController
from medicamentoController import medicamentoController

mis_usuario = userController()
mis_usuario.crear("Ariel","ariel","bautista",1)
mis_usuario.crear("Cesar","cesar","reyes",1)
mis_doctor = doctorController()
mis_enfermera = enfermeraController()
mis_medicamento = medicamentoController()

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


@app.route("/inicio-sesion", methods=['POST'])
def inicio_sesion():
    if request.method == 'POST':
        user_name = request.json['user_name'] 
        user_pass = request.json['user_pass']

    mi_usuario = mis_usuario.login(user_name,user_pass)
    if mi_usuario != None:
        return{
            'status': 100,
            'info': mi_usuario
        } 
    else:
        return{
            'status': 300,
            'info': "Invalid"
        }
    return{
        'status': 700,
        'info': "Mal request"
    }
    

@app.route("/usuario_crear", methods=['GET', 'POST', 'PUT', 'DELETE'])
def usuario_crear():

    response = {}

    if request.method == 'POST':
        nombre = request.json['nombre']
        user_name = request.json['user_name']
        user_pass = request.json['user_pass']
        rol = 2

        new_user = mis_usuario.crear(nombre,user_name,user_pass,rol)

        if (new_user != None):
            response['status'] = 100
            response['info'] = "usuario creado correctamente"+str(new_user)
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

@app.route("/doctor_crear", methods=['GET', 'POST', 'PUT', 'DELETE'])
def doctor_crear():

    response = {}

    if request.method == 'POST':
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        fecha = request.json['fecha']
        genero = request.json['genero']
        user_name = request.json['user_name']
        user_pass = request.json['user_pass']
        especialidad = request.json['especialidad']
        tel = request.json['tel']
        rol = 3

        
        new_doctor = mis_doctor.crear(nombre, apellido, fecha, genero, user_name, user_pass, especialidad, tel, rol)

        if (new_doctor != None):
            response['status'] = 100
            response['info'] = "usuario creado correctamente"+str(new_doctor)
        else:
            response['status'] = 300
            response['info'] = 'No se pudo realizar la acción'
    
    elif request.method == 'GET':
        id = int(request.args.get("id", None))
    
        return mis_doctor.devolver_usuario(id)

    elif request.method == 'DELETE':
        id = int(request.args.get("id", None))
        if mis_doctor.eliminar(id):
            response['status'] = 200
            response['info'] = "Usuario eliminado correctamente" 
        else: 
            response['status'] = 300
            response['info'] = 'No se pudo realizar la acción'

    return response


@app.route("/enfermera_crear", methods=['GET', 'POST', 'PUT', 'DELETE'])
def enfermera_crear():

    response = {}

    if request.method == 'POST':
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        fecha = request.json['fecha']
        genero = request.json['genero']
        user_name = request.json['user_name']
        user_pass = request.json['user_pass']
        tel = request.json['tel']
        rol = 4                

            
        new_enfermera = mis_enfermera.crear(nombre, apellido, fecha, genero, user_name, user_pass, tel, rol)

        if (new_enfermera != None):
            response['status'] = 100
            response['info'] = "usuario creado correctamente"+str(new_enfermera)
        else:
            response['status'] = 300
            response['info'] = 'No se pudo realizar la acción'
        
    elif request.method == 'GET':
        id = int(request.args.get("id", None))
        
        return mis_enfermera.devolver_usuario(id)

    elif request.method == 'DELETE':
        id = int(request.args.get("id", None))
        if mis_enfermera.eliminar(id):
            response['status'] = 200
            response['info'] = "Usuario eliminado correctamente" 
        else: 
            response['status'] = 300
            response['info'] = 'No se pudo realizar la acción'

    return response    

@app.route("/medicamento_crear", methods=['GET', 'POST', 'PUT', 'DELETE'])
def medicamento_crear():

    response = {}

    if request.method == 'POST':
        nombre = request.json['nombre']
        precio = request.json['precio']
        descripcion = request.json['descripcion']
        cantidad = request.json['cantidad']
        rol = 5            

        new_medicamento = mis_medicamento.crear(nombre, precio, descripcion, cantidad, rol)

        if (new_medicamento != None):
            response['status'] = 100
            response['info'] = "usuario creado correctamente"+str(new_medicamento)
        else:
            response['status'] = 300
            response['info'] = 'No se pudo realizar la acción'
        
    elif request.method == 'GET':
        id = int(request.args.get("id", None))
        
        return mis_medicamento.devolver_usuario(id)

    elif request.method == 'DELETE':
        id = int(request.args.get("id", None))
        if mis_medicamento.eliminar(id):
            response['status'] = 200
            response['info'] = "Usuario eliminado correctamente" 
        else: 
            response['status'] = 300
            response['info'] = 'No se pudo realizar la acción'

    return response

if __name__=="__main__":
    app.run(threaded=True, port=5001, debug=True)    

