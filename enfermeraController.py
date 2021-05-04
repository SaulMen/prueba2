from enfermera import enfermera
import json

class enfermeraController:

    def __init__(self):
        self.enfermera = []
        self.contador_id = 0

    #Método para hacer login 
    def login(self, user_name, user_pass):
        for enfr in self.enfermera:
            if enfr.autenticar(user_name, user_pass):
                return enfr.dump()
        return None
    
    #Método para crear usuario
    def crear(self, nombre, apellido, fecha, genero, user_name, user_pass, tel, rol):

        for enfr in self.enfermera:
            if enfr.user_name == user_name:
                print(f"El usuario {user_name} ya está en uso")
                return False

        self.enfermera.append(
            enfermera(self.contador_id, nombre, apellido, fecha, genero, user_name, user_pass, tel, rol)
        )
        print(f"Se creó el usuario: {user_name} con el id: {self.contador_id} de forma correcta ")
        self.contador_id += 1
        return True

    #Mostros ID del usuario
    def devolver_usuario(self, id):
        for enfr in self.enfermera:
            if enfr.id == id:
                return enfr.dump()
        return {}

    #Método para eliminar un usuario
    def eliminar(self, id):
        
        for enfr in self.enfermera:
            if enfr.id == id:
                #print(f"El usuario: {usr.user_name} ha sido eliminado con éxito ")
                self.enfermera.remove(enfr)
                return True 


    #Mostrar todos los usuarios
    def enlistar(self):
        for enfr in self.enfermera:
            print(enfr)

    def retornar_enfermeras(self):
        return ([enfr.dump() for enfr in self.enfermera])#json.dumps([enfr.dump() for enfr in self.enfermera])