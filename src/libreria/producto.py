class Producto:
    def __init__(self, nombre: str, precio_base: float):
        self.nombre = nombre
        self.precio_base = self._validar_precio_base(precio_base)

    def _validar_precio_base(self, precio_base: float) -> float:
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")
        return precio_base