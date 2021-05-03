class doctor:
    def __init__(self, id, nombre, apellido, fecha, genero, user_name, user_pass, especialidad, tel, rol):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha 
        self.genero = genero
        self.user_name = user_name
        self.user_pass = user_pass
        self.especialidad = especialidad
        self.tel = tel
        self.rol = rol
    
    def autenticar(self, user_name, user_pass):

        return (self.user_name == user_name and self.user_pass == user_pass)

    def actualizar_datos(self, nombre, apellido, fecha, genero, user_name, user_pass, especialidad, tel, rol ):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha 
        self.genero = genero
        self.user_name = user_name
        self.user_pass = user_pass
        self.especialidad = especialidad
        self.tel = tel
        self.rol = rol

    def dump(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'user_name': self.user_name,
            'especialidad': self.especialidad,
            'rol': self.rol
        }

    def __str__(self):
        return f"usuaio: [ id: {self.id}, nombre: {self.nombre}, user_name: {self.user_name}, user_pass: {self.user_pass}, rol: {self.rol}]"
