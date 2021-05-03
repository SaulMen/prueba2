class medicamento:
    def __init__(self, id, nombre, precio, descripcion, cantidad, rol):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion 
        self.cantidad = cantidad
        self.rol = rol
    

    def actualizar_datos(self, id, nombre, precio, descripcion, cantidad, rol):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion 
        self.cantidad = cantidad
        self.rol = rol

    def dump(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'cantidad': self.cantidad,
            'rol': self.rol
        }

    def __str__(self):
        return f"Medicamento: [ id: {self.id}, nombre: {self.nombre}, precio: {self.precio}, cantidad: {self.cantidad}, rol: {self.rol}]"
