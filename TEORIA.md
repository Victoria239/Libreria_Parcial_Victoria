# Sección teórica

## SM-1

Respuesta correcta: C.

La opción correcta es C porque describe el desarrollo tradicional con pruebas al final, donde los defectos se encuentran tarde y corregirlos suele ser más costoso.

## SM-2

Respuesta correcta: B.

La opción correcta es B porque en TDD primero debe existir un test que falle antes de escribir código de producción.

## PA-1

En TDD, el paso GREEN busca escribir solo el código necesario para que la prueba pase. No se trata todavía de hacer el código perfecto, sino de comprobar que la funcionalidad funciona. Si el desarrollador intenta hacer todo completo desde el inicio, puede agregar lógica que no está cubierta por pruebas. El código se mejora después, en el paso REFACTOR.

## PA-2

TDD se enfoca en probar el código desde el punto de vista técnico. Ayuda al desarrollador a construir funciones pequeñas y correctas. BDD se enfoca en describir el comportamiento esperado del sistema en lenguaje de negocio. TDD ayuda a validar cómo funciona internamente el código, mientras que BDD ayuda a validar que el sistema cumpla lo que necesita el usuario.

## PA-3

Tener 95% de cobertura no significa que el sistema no tenga errores. La cobertura solo indica que muchas líneas de código fueron ejecutadas por las pruebas. Pero una prueba puede estar mal diseñada y no validar el resultado correcto. Por ejemplo, puede probar que el precio final se calcula, pero no revisar si el descuento y el IVA se aplicaron en el orden correcto.

## PA-4

Probar solo el 20% no es suficiente porque ese valor está en la mitad del rango. También se deben probar los límites y valores inválidos. Para esta regla probaría -1%, 0%, 1%, 39%, 40% y 41%. Así valido que el sistema acepte los valores permitidos y rechace los que están fuera del rango.

## PA-5

TDD y BDD ayudan a tener pruebas automatizadas que luego pueden ejecutarse en un pipeline de CI/CD. Esto permite detectar errores cada vez que se sube código. Si el equipo no tiene buenas pruebas, el pipeline puede pasar aunque el sistema tenga fallas. Por eso las pruebas automatizadas son importantes para confiar en la integración y entrega continua.