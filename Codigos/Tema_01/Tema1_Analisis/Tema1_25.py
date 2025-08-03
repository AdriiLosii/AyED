"""
Una técnica de fuerza bruta para resolver un problema normalmente 
intenta agotar todas las posibilidades. Para el problema de detección 
de anagramas, podemos simplemente generar una lista de todas las cadenas 
posibles usando los caracteres de cadena1 y luego ver si se produce cadena2.
Sin embargo, hay una dificultad con este enfoque. Cuando se generan todas 
las cadenas posibles de cadena1, hay n posibles primeros caracteres, n−1 
posibles caracteres para la segunda posición, n−2 para la tercera, y así 
sucesivamente. El número total de cadenas candidatas es 
n∗(n−1)∗(n−2)∗...∗3∗2∗1, lo cual es n!. 
Aunque algunas de las cadenas pueden ser versiones duplicadas, el programa 
no puede saber esto de antemano y por tanto generá de todos modos n! 
cadenas diferentes.

Resulta que n! crece aún más rápido que 2n a medida que n se hace grande. 
De hecho, si cadena1 tuviera una longitud de 20 caracteres, habría 
20!=2.432.902.008.176.640.000 cadenas candidatas posibles. 
Si procesáramos una posibilidad cada segundo, aún así nos tomaría 
77.146.816.596 años el recorrido de la lista completa. Esto probablemente 
no va a ser una buena solución.

"""
