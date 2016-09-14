from defines import *


def fichas_eliminadas(matriz,punto_inicial,punto_final):
	x_1 = punto_inicial[0]
	y_1 = punto_inicial[1]
	x_2 = punto_final[0]
	y_2 = punto_final[1]
	if((x_1<x_2)and(y_1<y_2)):
		x_1+=1
		y_1+=1
		while(x_1<x_2):
			matriz[x_1][y_1] = 3
			x_1+=1
			y_1+=1

	elif((x_1<x_2)and(y_1>y_2)):
		x_1+=1
		y_1-=1
		while(x_1<x_2):
			matriz[x_1][y_1] = 3
			x_1+=1
			y_1-=1

def mover_ficha(matriz,punto_inicial,punto_final,ficha):
	x_1 = punto_inicial[0]
	y_1 = punto_inicial[1]
	x_2 = punto_final[0]
	y_2 = punto_final[1]
	matriz[x_2][y_2] = ficha
	if(ficha == FICHA_VERDE):
		fichas_eliminadas(matriz,(x_1,y_1),(x_2,y_2))
	else:
		fichas_eliminadas(matriz,(x_2,y_2),(x_1,y_1))

def calcular_victimas(matriz,punto_inicial,punto_final,ficha):
	x_1 = punto_inicial[0]
	y_1 = punto_inicial[1]
	x_2 = punto_final[0]
	y_2 = punto_final[1]

	# CALCULAR SI CUANDO SE HACE EL SALTO DE 2 en 2 HAY UNA FICHA CONTRICANTE Y DESPUES ESTA VACIO
	if(ficha == FICHA_VERDE):
		if((x_1<x_2)and(y_1<y_2) and matriz[x_1+1][y_1+1] == FICHA_ROJO and matriz[x_1+2][y_1+2] == VACIO):
			return True
		elif((x_1<x_2)and(y_1>y_2) and matriz[x_1+1][y_1-1] == FICHA_ROJO and matriz[x_1+2][y_1-2] == VACIO):
			return True
	else:
		if(((x_1>x_2)and(y_1>y_2)) and matriz[x_1-1][y_1-1] == FICHA_VERDE and matriz[x_1-2][y_1-2] == VACIO):
			return True
		elif((x_1>x_2)and(y_1<y_2) and matriz[x_1-1][y_1+1] == FICHA_VERDE and matriz[x_1-2][y_1+2] == VACIO):
			return True
	return False

def jugada_permitida(matriz,punto_inicial,punto_final, ficha):
	x_1 = punto_inicial[0]
	y_1 = punto_inicial[1]
	x_2 = punto_final[0]
	y_2 = punto_final[1]
	if(ficha == FICHA_VERDE):
		# CONDICION SI SE AVANZA HACIA DERECHA
		if(x_1+1==x_2 and y_1+1==y_2 and matriz[x_1+1][y_1+1] == VACIO):
			return True
		# CONDICION SI SE AVANZA HACIA IZQUIERDA
		elif(x_1+1==x_2 and y_1-1==y_2 and matriz[x_1+1][y_1-1] == VACIO):
			return True
		# CONDICION SI SE AVANZA HACIA DERECHA PERO AHORA CON SALTO sobre PIEZAS ROJAS
		elif(x_1+2==x_2 and y_1+2==y_2 and calcular_victimas(matriz,punto_inicial,punto_final,ficha)):
			return True
		elif(x_1+2==x_2 and y_1-2==y_2 and calcular_victimas(matriz,punto_inicial,punto_final,ficha)):
			return True
	# CONDICION PARA LA FICHA ROJA
	else:
		if(x_1-1==x_2 and y_1-1==y_2 and matriz[x_1-1][y_1-1] == VACIO):
			return True
		elif(x_1-1==x_2 and y_1+1==y_2 and matriz[x_1-1][y_1+1] == VACIO):
			return True
		elif(x_1-2==x_2 and y_1-2==y_2 and calcular_victimas(matriz,punto_inicial,punto_final,ficha)):
			return True
		elif(x_1-2==x_2 and y_1+2==y_2 and calcular_victimas(matriz,punto_inicial,punto_final,ficha)):
			return True
	return False

def posibles_jugadas(matriz, punto_inicial, ficha):
	lista_jugadas = []
	x_1 = punto_inicial[0]
	y_1 = punto_inicial[1]

	#JUGADAS DE PRIMER JUGADOR VERDE
	if(ficha == FICHA_VERDE):
		#COMPROBAR MOVIMIENTO Y SALTO DE 1 A 1  - DERECHO
		if(x_1+1<tam and x_1+1>-1 and y_1+1<tam and y_1+1>-1):
			#REVISARA SI LA CASILLA ESTA PERMITIDA (VACIA), SI ES ASI AGREGA ESA JUGADA
			if(jugada_permitida(matriz,punto_inicial,(x_1+1,y_1+1),ficha)):
				lista_jugadas.append((x_1+1,y_1+1))
		#COMPROBAR MOVIMIENTO Y SALTO DE 2 A 2  - DERECHO
		if(x_1+2<tam and x_1+2>-1 and y_1+2<tam and y_1+2>-1):
			if(jugada_permitida(matriz,punto_inicial,(x_1+2,y_1+2),ficha)):
				lista_jugadas.append((x_1+2,y_1+2))

		#COMPROBAR MOVIMIENTO Y SALTO DE 1 a 1  - IZQUIERDO
		if(x_1+1<tam and x_1+1>-1 and y_1-1<tam and y_1-1>-1):
			if(jugada_permitida(matriz,punto_inicial,(x_1+1,y_1-1),ficha)):
				lista_jugadas.append((x_1+1,y_1-1))

		#COMPROBAR MOVIMIENTO Y SALTO DE 2 a 2  - IZQUIERDO
		if(x_1+2<tam and x_1+2>-1 and y_1-2<tam and y_1-2>-1):
			if(jugada_permitida(matriz,punto_inicial,(x_1+2,y_1-2),ficha)):
				lista_jugadas.append((x_1+2,y_1-2))
	
	#JUGADAS DE PRIMER JUGADOR ROJO
	else:
		if(x_1-1<tam and x_1-1>-1 and y_1-1<tam and y_1-1>-1):
			if(jugada_permitida(matriz,punto_inicial,(x_1-1,y_1-1),ficha)):
				lista_jugadas.append((x_1-1,y_1-1))
		if(x_1-2<tam and x_1-2>-1 and y_1-2<tam and y_1-2>-1):
			if(jugada_permitida(matriz,punto_inicial,(x_1-2,y_1-2),ficha)):
				lista_jugadas.append((x_1-2,y_1-2))
		if(x_1-1<tam and x_1-1>-1 and y_1+1<tam and y_1+1>-1):
			if(jugada_permitida(matriz,punto_inicial,(x_1-1,y_1+1),ficha)):
				lista_jugadas.append((x_1-1,y_1+1))
		if(x_1-2<tam and x_1-2>-1 and y_1+2<tam and y_1+2>-1):
			if(jugada_permitida(matriz,punto_inicial,(x_1-2,y_1+2),ficha)):
				lista_jugadas.append((x_1-2,y_1+2))
	return lista_jugadas
