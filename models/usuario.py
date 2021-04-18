class usuario:

    #(int id, string name, string user_pass)
    def __init__(self, id, user_name, user_pass):
        self.id = id
        self.user_name = user_name
        self.user_pass = user_pass

    def autenticar(self, user_name, user_pass):
        self.saludar()
        return (self.user_name == user_name and self.user_pass == user_pass)
        
    def saludar(self):
        print("Ahora si jeje x3")

usuario1 = usuario(1, "saul", "xd")
usuario1.saludar()