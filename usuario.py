class usuario:

    #(int id, string name, string user_pass)
    def __init__(self, id, nombre, user_name, user_pass, rol):
        self.id = id
        self.nombre = nombre
        self.user_name = user_name
        self.user_pass = user_pass
        self.rol = rol

    def autenticar(self, user_name, user_pass):

        return (self.user_name == user_name and self.user_pass == user_pass)

    def actualizar_datos(self, nombre, user_name, user_pass, rol ):
        self.id = id
        self.nombre = nombre
        self.user_name = user_name
        self.user_pass = user_pass
        self.rol = rol

    def dump(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'user_name': self.user_name,
            'rol': self.rol
        }

    def num_id(self, numId):
        self.num_Id = id
        return self.num_Id

    def __str__(self):
        return f"usuaio: [ id: {self.id}, nombre: {self.nombre}, user_name: {self.user_name}, user_pass: {self.user_pass}, rol: {self.rol}]"
