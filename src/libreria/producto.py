class Producto:
    DESCUENTO_MINIMO = 0
    DESCUENTO_MAXIMO = 40
    IVA = 0.19

    def __init__(self, nombre: str, precio_base: float):
        self.nombre = nombre
        self.precio_base = self._validar_precio_base(precio_base)
        self.descuento = 0

    def _validar_precio_base(self, precio_base: float) -> float:
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")
        return precio_base

    def aplicar_descuento(self, descuento: float):
        self.descuento = self._validar_descuento(descuento)

    def _validar_descuento(self, descuento: float) -> float:
        if descuento < self.DESCUENTO_MINIMO or descuento > self.DESCUENTO_MAXIMO:
            raise ValueError("El descuento debe estar entre 0% y 40%")
        return descuento

    def calcular_precio_final(self) -> float:
        precio_con_descuento = self.precio_base - (self.precio_base * self.descuento / 100)
        precio_final = precio_con_descuento + (precio_con_descuento * self.IVA)

        if precio_final < 0:
            return 0

        return precio_final