from flask import Flask, request
from flask_cors import CORS
from usuario import usuario
from datetime import datetime as dt
from userController import userController
from doctor import doctor
from doctorController import doctorController
from enfermeraController import enfermeraController
from medicamentoController import medicamentoController
import json

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

    mi_doctor = mis_doctor.login(user_name, user_pass)

    mi_enfermera = mis_enfermera.login(user_name, user_pass)

    if mi_usuario != None:
        print("entró 1")
        return{
            'status': 100,
            'info': mi_usuario
        }
    elif mi_doctor != None:
        print("entró 2")
        return{
            'status': 100,
            'info': mi_doctor
        }
    elif mi_enfermera != None:
        print("entró 3")
        return{
            'status': 100,
            'info': mi_enfermera
        }
    else:
        print("entró 3")
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

@app.route("/obtener_usuarios", methods=['GET'])
def obtener_usuarios():
    
    return {
        'status': 100,
        'info': mis_usuario.retornar_usuarios()
    }

@app.route("/obtener_doctores", methods=['GET'])
def obtener_doctores():
    
    return {
        'status': 100,
        'info': mis_doctor.retornar_doctores()
    }

@app.route("/obtener_enfermeras", methods=['GET'])
def obtener_enfermeras():
    
    return {
        'status': 100,
        'info': mis_enfermera.retornar_enfermeras()
    }

@app.route("/obtener_medicamentos", methods=['GET'])
def obtener_medicamentos():
    
    return {
        'status': 100,
        'info': mis_medicamento.retornar_medicamentos()
    }

@app.route("/obtener_un_usuario", methods=['POST'])
def obtener_un_usuario():
    if request.method == 'POST':
        id = request.json['id']
        
    mi_usuario2 = mis_usuario.devolver_usuario(id)

    if mi_usuario2 != None:
        print("entró 1")
        return{
            'status': 100,
            'info': mi_usuario2
        }

@app.route("/eliminar_usuario", methods=['POST'])
def eliminar_usuario():
    if request.method == 'POST':
        id = request.json['id']
        
    mi_usuario3 = mis_usuario.eliminar(id)

    if mi_usuario3 == True:
        print("entró 2")
        return{
            'status': 100,
            'info': mi_usuario3
        }
    else:
        return{
            'status': 300,
            'info': "mi_usuario3"
        }

@app.route("/eliminar_doctor", methods=['POST'])
def eliminar_doctor():
    if request.method == 'POST':
        id = request.json['id']
        
    mi_doctor = mis_doctor.eliminar(id)

    if mi_doctor == True:
        print("entró 2")
        return{
            'status': 100,
            'info': mi_doctor
        }
    else:
        return{
            'status': 300,
            'info': "mi_usuario3"
        }

@app.route("/eliminar_enfermera", methods=['POST'])
def eliminar_enfermera():
    if request.method == 'POST':
        id = request.json['id']
        
    mi_enfermera = mis_enfermera.eliminar(id)

    if mi_enfermera == True:
        print("entró 2")
        return{
            'status': 100,
            'info': mi_enfermera
        }
    else:
        return{
            'status': 300,
            'info': "mi_usuario3"
        }

@app.route("/eliminar_medicamento", methods=['POST'])
def eliminar_medicamento():
    if request.method == 'POST':
        id = request.json['id']
        
    mi_medicamento = mis_medicamento.eliminar(id)

    if mi_medicamento == True:
        print("entró 2")
        return{
            'status': 100,
            'info': mi_medicamento
        }
    else:
        return{
            'status': 300,
            'info': "mi_usuario3"
        }

if __name__=="__main__":
    app.run(threaded=True, port=5001, debug=True)  

