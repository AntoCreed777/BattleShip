Integrantes del grupo:

	Antonio Benavidez Puentes
	Pablo Villagran Hermanns
	Renato Galan Quiroz
	Lucas Morales Oyanedel


Instrucciones de juego:

Paso 1: Tamaño del tablero

	Le aparecerá el siguiente mensaje: "Ingrese el tamaño del tablero:"

	Debera ingresar un número entero mayor o igual a "10" y menor o igual a "1000" ej: 

		Si escogió un tamaño de tablero de "10", se formará una cuadrícula de tamaño de "10x10" que va desde "1 a 10" vertical y horizontalmente
		como en un plano cartesiano 
		

Paso 2: Cantidad de barcos en juego

	Le aparecerá el siguiente mensaje: "Ingrese la cantidad de barcos en juego por jugador:"

	Deberá ingresar un número mayor o igual a "2" y menor o igual a el tamaño de su tablero escogido, ej:

		Si escogió un tamaño de mapa de "10", el número entero debe ser mayor o igual a "2" y menor o igual a "10".


Paso 3: Posición y orientación de los barcos

	Le aparecerá el mensaje "Ingrese la Coordenada Central 'X'de su 1°barco:" 
	
	Deberá ingresar un número para "X" dentro del rango de su tablero, ej:

		Si escogió un tamaño de tablero de "10", deberá ingresar un número entero mayor o igual a "1" y menor o igual a "10".


	A continuación le aparecerá el mensaje "Ingrese la Coordenada Central 'Y'de su 1°barco:" 
	
	Deberá ingresar un número para "Y" dentro del rango de su tablero, ej:

		Si escogió un tamaño de tablero de "10", deberá ingresar un número entero mayor o igual a "1" y menor o igual a "10".
			

	Luego se le mostrará el mensaje "Ingrese la horientacion de su 1°Barco(V o H):"

	Si desea orientar el barco de manera vertical, deberá escribir la letra "v" o "V"

	Si desea orientar el barco de manera horizontal, deberá escribir la letra "h" o "H"
	
	Una vez ingresada la posición y orientación de los barcos, le aparecerá el siguiente mensaje "Estas son las coordenadas de su barco", seguido de las
	coordenadas que proporcionó. Bajo este mensaje le aparecerá una cuadrícula que contiene las letras "B" y "P". Las letras "B" corresponden a 
	la posición de su barco y las letras "P", corresponden a un perímetro alrededor de los barcos en donde no podrá posicionar otro barco. Las 	coordenadas del mapa empiezan en el punto (1,1) (esquina inferior izquierda). Estas aumentan en "X" hacia la derecha y en "Y" hacia arriba como en 
	un plano cartesiano.

	Este proceso ocurrirá hasta que haya ubicado todos sus barcos.


Paso 3.1: Excepciones en las posiciones y orientaciones de los barcos

	Digamos que escogió un tamaño de tablero de "10":

		-Podrá ingresar la posición de los barcos en las coordenadas que contengan las letras "P". Pero le pedirá ingresar nuevamente la posición

		-Podrá ingresar la posición de los barcos en las esquinas del tablero, sean (1,1) , (1,10) , (10,1) , (10,10). Pero le pedirá ingresar 			 nuevamente la posición

		-Podrá ingresar la orientación de los barcos en los bordes superior e inferior de manera vertical. Pero le pedirá ingresar nuevamente la 		 posición iniciando nuevamente el proceso

		-Podrá ingresar la orientación de los barcos en los bordes laterales (derecha e izquierda) de manera horizontal. Pero le pedirá ingresar 		 nuevamente la posición iniciando nuevamente el proceso


Paso 4: Inicio del juego

	Si desea iniciar usted el juego deberá escribir el mensaje "jugador". 
	
	Si desea que la computadora inicie el juego, deberá escribir el mensaje "computadora"


Paso 5: Secuencia de turnos (Caso 1 y Caso 2)


	Caso 1: Si escogió que comenzara la computadora, le aparecera el siguiente mensaje "El enemigo" seguido de una de dos variantes:

		-Variante 1: "no nos ha dado". Significando que la computadora no ha dado a uno de sus barcos

		-Variante 2: "nos ha dado en un barco!!". Significando que la computadora le ha dado a uno de sus barcos.

	 Seguido del turno de la computadora comienza el suyo, deberá ingresar las coordenadas de ataque hacia los barcos de la computadora:

		-Le aparecerá el siguiente mensaje: "Ingrese la Coordenada de ataque 'X':". En donde deberá ingresar un número entero mayor o igual a "1" y 
		 menor o igual al tamaño de su tablero, ej:

			Si escogió un tamaño de tablero de "10", su coordenada de ataque en "X" deberá ser un número entero mayor o igual a "1" y menor o 			igual a "10"

		-Luego de ingresar la coordenada de ataque de "x", le aparecerá el siguiente mensaje: "Ingrese la Coordenada de ataque 'Y':". En donde 			 deberá ingresar un número entero mayor o igual a "1" y menor o igual al tamaño de su tablero, ej:

			Si escogió un tamaño de tablero de "10", su coordenada de ataque en "Y" deberá ser un número entero mayor o igual a "1" y menor o 			igual a "10"

		 Después de haber ingresado las coordenadas de ataque, le aparecerá uno de dos mensajes:

			-Mensaje 1: "Has dado en un barco". Significando que ha dado en un barco enemigo.
			
			-Mensaje 2: "Has dado al agua". Significando que no ha dado en un barco enemigo.

	 Luego de su primer ataque, se le brindará con una cuadrícula con las coordenadas de sus ataques.


	Caso 2: Si escogió comenzar usted, deberá ingresar las coordenadas de ataque hacia los barcos de la computadora:

		-Le aparecerá el siguiente mensaje: "Ingrese la Coordenada de ataque 'X':". En donde deberá ingresar un número entero mayor o igual a "1" y 
		 menor o igual al tamaño de su tablero, ej:

			Si escogió un tamaño de tablero de "10", su coordenada de ataque en "X" deberá ser un número entero mayor o igual a "1" y menor o 			igual a "10"

		-Luego de ingresar la coordenada de ataque de "x", le aparecerá el siguiente mensaje: "Ingrese la Coordenada de ataque 'Y':". En donde 			 deberá ingresar un número entero mayor o igual a "1" y menor o igual al tamaño de su tablero, ej:

			Si escogió un tamaño de tablero de "10", su coordenada de ataque en "Y" deberá ser un número entero mayor o igual a "1" y menor o 			igual a "10"

		 Después de haber ingresado las coordenadas de ataque, le aparecerá uno de dos mensajes:

			-Mensaje 1: "Has dado en un barco". Significando que ha dado en un barco enemigo.
			
			-Mensaje 2: "Has dado al agua". Significando que no ha dado en un barco enemigo.

		 Luego de su primer ataque, se le brindará con una cuadrícula con las coordenadas de sus ataques.

		-Después de su ataque viene el turno de la computadora, le aparecera el siguiente mensaje "El enemigo" seguido de una de dos variantes:

			-Variante 1: "no nos ha dado". Significando que la computadora no ha dado a uno de sus barcos

			-Variante 2: "nos ha dado en un barco!!". Significando que la computadora le ha dado a uno de sus barcos.


La secuencia de turnos continuará hasta que usted o la computadora se queden sin barcos.

Paso 5.1: Excepciones en los disparos y barcos hundidos

	Excepciones:
	
		-No podrá atacar en punto fuera del tablero, ej: 

			si escogio un tamaño de tablero de "10" y ataca en la posición (11,11) le aparecerá el mensaje "Ingrese nuevamente la Coordenada de 			ataque 'X':" seguido del mensaje "Ingrese nuevamente la Coordenada de ataque 'Y':". Porque el punto (11,11) no pertence al tablero.

		-No podrá atacar más de una ves en el mismo punto, ej:

			si escogio un tamaño de tablero de "10" y ataca en la posición (10,10) le aparecerá el mensaje "Ingrese nuevamente la Coordenada de 			ataque 'X':" seguido del mensaje "Ingrese nuevamente la Coordenada de ataque 'Y':". Porque el punto (10,10) ya ha sido reemplazado 			con una "X" que simboliza que ha atacado esa posición 

	Barcos hundidos:

		-Si la computadora ha hundido un barco suyo, aparecerá el mensaje "!!!NOS HAN HUNDIDO UN BARCO, DEBEMOS RESPONDER!!!"

		-Si ha hundido un barco de la computadora aparecerá el mensaje "!!!BARCO HUNDIDO, CADA VES MÁS CERCA DE LA VICTORIA CAMARADA!!!"


Paso 6: Fin del juego

	SI ha acabado con todos los barcos enemigos, aparecerá el mensaje "Bien hecho camarada, habéis demostrado vuestra valia, POR LA MADRE PATRIA!!!!!"

	Si la computadora ha acabado con todos sus barcos, aparecerá el mensaje "NOS HAN DERROTADO, RETIRADAAAA!!!!"


