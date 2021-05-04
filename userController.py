from usuario import usuario
import json

class userController:

    #Constructor
    def __init__(self):
        self.usuarios = []
        self.contador_id = 0

    #Método para hacer login 
    def login(self, user_name, user_pass):
        for usr in self.usuarios:
            if usr.autenticar(user_name, user_pass):
                return usr.dump()
        return None
    
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
        return None

    #Método para eliminar un usuario
    def eliminar(self, id):
        
        for usr in self.usuarios:
            if usr.id == id:
                #print(f"El usuario: {usr.user_name} ha sido eliminado con éxito ")
                self.usuarios.remove(usr)
                return True        


    #Mostrar todos los usuarios
    def enlistar(self):
        for usr in self.usuarios:
            print(usr)

    def retornar_usuarios(self):
        return ([usr.dump() for usr in self.usuarios])#json.dumps([usr.dump() for usr in self.usuarios])