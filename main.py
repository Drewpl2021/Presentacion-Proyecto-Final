class Comprobante:
    def __init__(self,ruc, dni, nombre_apellido, fecha,codigo_producto, cantidad_de_producto,precio,total):
        self.ruc = ruc
        self.dni = dni
        self.nombre_apellido = nombre_apellido
        self.fecha = fecha
        self.producto = codigo_producto
        self.cantidad_de_producto = cantidad_de_producto
        self.precio = precio
        self.total = total

    def __str__(self):
        return "{};{};{};{};{};{};{};{}\n".format(
            self.ruc, self.dni, self.nombre_apellido, self.fecha, self.producto, self.cantidad_de_producto, self. precio, self.total
        )
#------------------------------------------------------------
class Clientes:
    def __init__(self, Dni, nombre_apellido,direccion ,telefono,email):
        self.Dni = Dni
        self.nombre_apellido = nombre_apellido
        self.dirrecion = direccion
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return "{};{};{};{};{}\n".format(
            self.Dni, self.nombre_apellido, self.dirrecion, self.telefono, self.email
        )
#--------------------------------------------------------------
class Clientes2:
    def __init__(self, Dni):
        self.Dni = Dni

    def __str__(self):
        return "{};\n".format(self.Dni)
