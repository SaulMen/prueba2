from medicamento import medicamento
import json

class medicamentoController:

    def __init__(self):
        self.medicamento = []
        self.contador_id = 0

    #Método para hacer login 
    def login(self, nombre, precio):
        for mdct in self.medicamento:
            if mdct.autenticar(nombre, precio):
                return mdct.dump()
        return None
    
    #Método para crear usuario
    def crear(self, nombre, precio, descripcion, cantidad, rol):

        for mdct in self.medicamento:
            if mdct.nombre == nombre:
                print(f"El medicamento {nombre} ya se ingresó")
                return False

        self.medicamento.append(
            medicamento(self.contador_id, nombre, precio, descripcion, cantidad, rol)
        )
        print(f"Se agregó el medicamento: {nombre} con el id: {self.contador_id} de forma correcta ")
        self.contador_id += 1
        return True

    #Mostros ID del usuario
    def devolver_usuario(self, id):
        for mdct in self.medicamento:
            if mdct.id == id:
                return mdct.dump()
        return {}

    #Método para eliminar un usuario
    def eliminar(self, id):
        for mdct in self.medicamento:

            if mdct.id == id:
                print(f"El medicamento: {mdct.nombre} ha sido eliminado con éxito ")
                self.medicamento.remove(mdct)
                return True

            print(f"El medicamento con id: {id} no ha encontrado.")
            return False 


    #Mostrar todos los usuarios
    def enlistar(self):
        for mdct in self.medicamento:
            print(mdct)

    def retornar_medicamentos(self):
        return json.dumps([mdct.dump() for mdct in self.medicamento])