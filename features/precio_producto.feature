Feature: Cálculo del precio final de productos de la librería
  Como administrador de la Librería del Centro
  Quiero aplicar descuentos válidos y calcular el precio final con IVA
  Para vender productos con precios correctos y reglas claras

  Background:
    Given existe un producto llamado "Libro" con precio base 10000

  @descuento @borde
  Scenario: Aplicar descuento mínimo permitido
    When aplico un descuento de 0
    Then el descuento del producto debe ser 0

  @descuento @positivo
  Scenario: Aplicar descuento válido intermedio
    When aplico un descuento de 20
    Then el descuento del producto debe ser 20

  @descuento @borde
  Scenario: Aplicar descuento máximo permitido
    When aplico un descuento de 40
    Then el descuento del producto debe ser 40

  @descuento @error
  Scenario: Rechazar descuento superior al permitido
    When intento aplicar un descuento de 41
    Then el sistema debe mostrar el error "El descuento debe estar entre 0% y 40%"

  @precio_final @positivo
  Scenario Outline: Calcular precio final aplicando primero descuento y luego IVA
    When aplico un descuento de <descuento>
    And calculo el precio final
    Then el precio final debe ser <precio_final>

    Examples:
      | descuento | precio_final |
      | 0         | 11900        |
      | 10        | 10710        |
      | 40        | 7140         |