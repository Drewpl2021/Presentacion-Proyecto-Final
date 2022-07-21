#--------------------------------------------
class Producto:
    def __init__(self, codigo, marca, color, talla, genero, precio):
        self.codigo = codigo
        self.marca = marca
        self.color = color
        self.talla = talla
        self.genero = genero
        self.precio = precio
    def __str__(self):
        return "{};{};{};{};{};{}\n".format(self.codigo, self.marca, self.color, self.talla, self.genero, self.precio)
#------------------------------------------------------
class Editar:
    def __init__(self, codigo, marca, color, talla, genero, precio):
        self.codigo = codigo
        self.marca = marca
        self.color = color
        self.talla = talla
        self.genero = genero
        self.precio = precio
    def __str__(self):
        return "{};{};{};{};{};{}\n".format(self.codigo, self.marca, self.color, self.talla, self.genero, self.precioi)
#-------------------------------------------------------
class Clientes:
    def __init__(self, Dni, nombre_apellido,direccion ,telefono,email):
        self.Dni = Dni
        self.nombre_apellido = nombre_apellido
        self.dirrecion = direccion
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return "{};{};{};{};{}\n".format(
            self.Dni, self.nombre_apellido, self.dirrecion, self.telefono, self.email)
#---------------------------------------------------------
class Clientes2:
    def __init__(self, nombre_apellido):
        self.nombre_apellido = nombre_apellido
 
    def __str__(self):
        return "{}\n".format(self. self.nombre_apellido)
#---------------------------------------------------------
class Productos2:
    def __init__(self, precio):
        self.precio = precio
    def __str__(self):
        return "{}\n".format( self.precio)

