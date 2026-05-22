# Parcial Librería del Centro - Victoria

## Análisis de reglas

### Regla 1: Producto con nombre y precio base mayor que cero

| Partición | Tipo | Valor representativo | Resultado esperado |
|---|---|---:|---|
| Precio base mayor que cero | Válida | 10000 | Producto creado correctamente |
| Precio base igual a cero | Inválida | 0 | Rechazar producto con mensaje claro |
| Precio base menor que cero | Inválida | -5000 | Rechazar producto con mensaje claro |

### Regla 2: Descuento entre 0% y 40%

| Partición | Tipo | Valor representativo | Resultado esperado |
|---|---|---:|---|
| Descuento igual a 0% | Válida | 0 | Descuento aceptado |
| Descuento entre 1% y 39% | Válida | 20 | Descuento aceptado |
| Descuento igual a 40% | Válida | 40 | Descuento aceptado |
| Descuento menor que 0% | Inválida | -1 | Rechazar descuento con mensaje claro |
| Descuento mayor que 40% | Inválida | 41 | Rechazar descuento con mensaje claro |

### Análisis de valores límite para Regla 2

| Valor | Tipo | Resultado esperado |
|---:|---|---|
| -1 | Inválido | Rechazar descuento |
| 0 | Borde válido | Aceptar descuento |
| 1 | Válido | Aceptar descuento |
| 39 | Válido | Aceptar descuento |
| 40 | Borde válido | Aceptar descuento |
| 41 | Inválido | Rechazar descuento |

### Pregunta para Regla 3

Pregunta: ¿El IVA del 19% debe redondearse a decimales, a entero, o conservar el valor exacto?

Justificación: Es necesario definir el criterio de redondeo para que los cálculos del precio final sean consistentes y las pruebas puedan validar un resultado exacto.

## Casos de prueba

| ID | Regla | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| CP01 | Regla 1 | Crear producto con precio válido | No existe producto creado | Nombre: Libro, precio: 10000 | Crear producto | Producto creado correctamente | Positivo |
| CP02 | Regla 1 | Crear producto con precio cero | No existe producto creado | Nombre: Libro, precio: 0 | Crear producto | El sistema rechaza el producto con mensaje claro | Negativo |
| CP03 | Regla 1 | Crear producto con precio negativo | No existe producto creado | Nombre: Libro, precio: -5000 | Crear producto | El sistema rechaza el producto con mensaje claro | Negativo |
| CP04 | Regla 2 | Aplicar descuento de 0% | Producto válido creado | Precio: 10000, descuento: 0 | Aplicar descuento | El descuento es aceptado | Borde |
| CP05 | Regla 2 | Aplicar descuento intermedio | Producto válido creado | Precio: 10000, descuento: 20 | Aplicar descuento | El descuento es aceptado | Positivo |
| CP06 | Regla 2 | Aplicar descuento de 40% | Producto válido creado | Precio: 10000, descuento: 40 | Aplicar descuento | El descuento es aceptado | Borde |
| CP07 | Regla 2 | Aplicar descuento mayor al permitido | Producto válido creado | Precio: 10000, descuento: 41 | Aplicar descuento | El sistema rechaza el descuento con mensaje claro | Negativo |
| CP08 | Regla 3 | Calcular precio final con descuento e IVA | Producto válido creado | Precio: 10000, descuento: 10 | Calcular precio final | Primero aplica descuento y luego IVA del 19% | Positivo |
| CP09 | Regla 3 | Calcular precio final sin descuento | Producto válido creado | Precio: 10000, descuento: 0 | Calcular precio final | Precio final igual a 11900 | Borde |