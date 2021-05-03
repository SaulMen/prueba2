from doctor import doctor
import json

class doctorController:
     
    def __init__(self):
         self.doctores = []
         self.contador_id = 0

    #Método para hacer login 
    def login(self, user_name, user_pass):
        print(user_name +"   " +user_pass)
        for dtr in self.doctores:
            if dtr.autenticar(user_name, user_pass):
                return dtr.dump()
        return None
    
    #Método para crear usuario
    def crear(self, nombre, apellido, fecha, genero, user_name, user_pass, especialidad, tel, rol):

        for dtr in self.doctores:
            if dtr.user_name == user_name:
                print(f"El usuario {user_name} ya está en uso")
                return False

        self.doctores.append(
            doctor(self.contador_id, nombre, apellido, fecha, genero, user_name, user_pass, especialidad, tel, rol)
        )
        print(f"Se creó el usuario: {user_name} con el id: {self.contador_id} de forma correcta ")
        self.contador_id += 1
        return True

    #Mostros ID del usuario
    def devolver_usuario(self, id):
        for dtr in self.doctores:
            if dtr.id == id:
                return dtr.dump()
        return {}

    #Método para eliminar un usuario
    def eliminar(self, id):
        for dtr in self.doctores:

            if dtr.id == id:
                print(f"El usuario: {dtr.user_name} ha sido eliminado con éxito ")
                self.doctores.remove(dtr)
                return True

            print(f"El usuario con id: {id} no ha encontrado.")
            return False 


    #Mostrar todos los usuarios
    def enlistar(self):
        for dtr in self.doctores:
            print(dtr)

    def retornar_doctores(self):
        return json.dumps([dtr.dump() for dtr in self.doctores])

    
    