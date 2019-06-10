# Pruebas de Código

El objetivo es resolver el problema, utilizando Python3 
como lenguaje y Git para compartir el código.

## Problema

Se debe leer información desde una página web repetidas veces y mostrar esa información en la pantalla.
En este caso, se trata de obtener un número al azar (un dado virtual) desde la página [http://olympus.realpython.org/dice]()

El programa debe pedir 6 veces el resultado, esperando 10 
segundos entre intentos y mostrarlo en la salida de la línea 
de comando, con este formato:

`Me salió un '<VALOR>' el día <FECHA>`

Ejemplo:

	Me salió un '1' el día June 10, 2019 02:58:29P
	Me salió un '3' el día June 10, 2019 02:58:39P
	Me salió un '5' el día June 10, 2019 02:58:50P
	Me salió un '2' el día June 10, 2019 02:59:01P
	Me salió un '1' el día June 10, 2019 02:59:11P
	Me salió un '4' el día June 10, 2019 02:59:21P

Se invocará al programa de la siguiente manera:
`python3 obtener_numero_azar.py`

## Indicaciones
1. El valor del dado está en el tag `id=result`.
2. La fecha está en el tag `id=time`
3. Utilizar el módulo`mechanicalsoup`.
Se puede instalar con `pip3 install mechanicalsoup`
4. Usar python3

