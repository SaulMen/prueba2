from usuario import usuario
import json

class userController:

    #Constructor
    def __init__(self):
        self.usuarios = []
        self.contador_id = 0

    #Método para crear usuario
    def crear(self, nombre, user_name, user_pass, rol):

        for usr in self.usuarios:
            if usr.user_name == user_name:
                print(f"El usuario {user_name} ya está en uso")
                return False

        self.usuarios.append(
            usuario(self.contador_id, nombre, user_name, user_pass, rol)
        )
        print(f"Se creó el usuario: {user_name} con el id: {self.contador_id} de forma correcta ")
        self.contador_id += 1
        return True

    #Mostros ID del usuario
    def devolver_usuario(self, id):
        for usr in self.usuarios:
            if usr.id == id:
                return usr.dump()
        return {}

    #Método para eliminar un usuario
    def eliminar(self, id):
        for usr in self.usuarios:

            if usr.id == id:
                print(f"El usuario: {usr.user_name} ha sido eliminado con éxito ")
                self.usuarios.remove(usr)
                return True

            print(f"El usuario con id: {id} no ha encontrado.")
            return False 


    #Mostrar todos los usuarios
    def enlistar(self):
        for usr in self.usuarios:
            print(usr)

    def retornar_usuarios(self):
        return json.dumps([usr.dump() for usr in self.usuarios])