# Sección teórica

## SM-1

Respuesta correcta: C.

A es incorrecta porque shift-left testing busca probar desde etapas tempranas, no dejar las pruebas para el final.  
B es incorrecta porque shift-right testing se enfoca más en validar en producción o después del despliegue.  
D es incorrecta porque integración continua se refiere a automatizar integración, pruebas y validaciones, no a probar al final.  

La opción correcta es C porque describe el desarrollo tradicional con pruebas al final, donde los defectos se encuentran tarde y corregirlos suele ser más costoso.

## SM-2

Respuesta correcta: B.

A es incorrecta porque el refactor ocurre después de tener pruebas en verde, no antes de escribirlas.  
C es incorrecta porque el problema principal no es cubrir muchos casos, sino haber escrito código antes del test.  
D es incorrecta porque TDD no permite escribir primero el código de producción y luego los tests.  

La opción correcta es B porque en TDD primero debe existir un test que falle antes de escribir código de producción.

## PA-1

En TDD, el paso GREEN consiste en escribir el código mínimo necesario para que el test pase. La idea no es hacer desde el inicio la solución más completa, sino avanzar de forma controlada, validando cada comportamiento con una prueba. Si el desarrollador intenta escribir código limpio y completo desde el primer GREEN, puede agregar lógica que todavía no está protegida por tests. Eso rompe la disciplina de TDD porque se deja de construir desde la necesidad real de cada prueba. El código limpio llega después, en el paso REFACTOR, cuando ya existe una prueba que confirma que el comportamiento sigue funcionando.

## PA-2

TDD y BDD se parecen porque ambos usan pruebas para guiar el desarrollo, pero resuelven problemas distintos. TDD ayuda principalmente al desarrollador a construir código correcto desde pruebas pequeñas y técnicas. BDD ayuda a expresar el comportamiento esperado del sistema en lenguaje de negocio, para que sea entendible por usuarios, analistas, QA y desarrolladores. TDD se enfoca más en unidades de código, mientras que BDD se enfoca en escenarios de comportamiento. Se complementan porque TDD asegura la calidad interna del código y BDD ayuda a validar que el sistema haga lo que el negocio espera.

## PA-3

Tener 95% de cobertura no significa que el sistema no tenga errores. La cobertura solo indica qué porcentaje del código fue ejecutado por las pruebas, pero no garantiza que las pruebas estén bien diseñadas. Por ejemplo, una prueba puede ejecutar el método que calcula el precio final, pero verificar solo que retorne un número, sin validar si aplicó correctamente el descuento y el IVA. En ese caso habría cobertura, pero el cálculo podría estar mal. Por eso es más importante combinar buena cobertura con casos relevantes, valores límite, negativos y positivos.

## PA-4

La lógica de probar solo 20% es incorrecta porque 20% está en el centro del rango válido, pero no prueba los límites ni los valores inválidos. Para la regla del descuento entre 0% y 40%, se deben probar valores como 0%, 1%, 39%, 40% y 41%. También conviene probar un valor negativo como -1%. El 0% y el 40% son importantes porque son los bordes permitidos. El 41% y el -1% sirven para comprobar que el sistema rechaza valores fuera del rango.

## PA-5

TDD y BDD se conectan con CI/CD porque permiten tener una suite de pruebas automatizadas que se puede ejecutar cada vez que se sube código al repositorio. En un pipeline de CI/CD, las pruebas ayudan a detectar errores antes de integrar o desplegar cambios. Si el equipo no tiene pruebas automatizadas sólidas, el pipeline puede pasar aunque el sistema tenga defectos importantes. Eso reduce la confianza en la integración continua y obliga a depender demasiado de pruebas manuales. Por eso TDD y BDD fortalecen el pipeline al validar tanto el código como el comportamiento esperado.