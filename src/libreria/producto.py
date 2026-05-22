class Producto:
    def __init__(self, nombre, precio_base):
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")

        self.nombre = nombre
        self.precio_base = precio_base