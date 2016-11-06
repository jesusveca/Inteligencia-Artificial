import pygame
from defines import *
from tablero import *
from juego import *
from poda_alfa_beta import *
from arbol import *

def main():
	grid = crear_tablero()
	# Inicializamos pygame
	pygame.init()
	# Establecemos el LARGO y ALTO de la pantalla
	DIMENSION_VENTANA = [width, height]
	pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
	#Titulo
	pygame.display.set_caption("Damas IA-Minimax-Alfa-Beta-Poda - 2016-ii - TICONA_VERA")
	done = False
	reloj = pygame.time.Clock()
	TURNO = 1
	PUSH = 0
	jugadas = []
	ficha_seleccionada = [0,(0,0)]

	while not done:
		for evento in pygame.event.get(): 
			# PARA SALIR DEL JUEGO CON ESCAPE O DESDE TERMINAL
			if (evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == 27)):
				done = True
			#PIEZAS VERDES
			# saber de donde viene el movimiento
			elif (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT and TURNO == 1):
				# jugadas = []
				pos = pygame.mouse.get_pos() #obtener posicion actual de mouse
				columna_inicio = ((pos[0]- xGrid)/ (LARGO + MARGEN)) 
				fila_inicio = ((pos[1]-yGrid) / (ALTO + MARGEN))
				if(columna_inicio>-1 and columna_inicio<tam and fila_inicio >-1 and fila_inicio <tam):
					if (grid[fila_inicio][columna_inicio] == 1):
						grid[fila_inicio][columna_inicio] = 3
						ficha_seleccionada[0]=FICHA_VERDE
						ficha_seleccionada[1]=(fila_inicio,columna_inicio)

						#posibles jugadas le paso una matriz, una posicion inicial y una ficha
						jugadas = posibles_jugadas(grid,(fila_inicio,columna_inicio),FICHA_VERDE)
						PUSH = 1

				# Confirmar el movimiento hacia donde se ira
			elif (evento.type == pygame.MOUSEBUTTONUP and evento.button == LEFT and TURNO==1 and PUSH==1):
				pos = pygame.mouse.get_pos()
				columna_destino = ((pos[0]- xGrid)/ (LARGO + MARGEN))
				fila_destino = ((pos[1]-yGrid) / (ALTO + MARGEN))
				if(columna_destino>-1 and columna_destino<tam and fila_destino>-1 and fila_destino<tam):
					if ((fila_destino,columna_destino)in jugadas):
						jugadas = []
						mover_ficha(grid,(fila_inicio,columna_inicio),(fila_destino,columna_destino),FICHA_VERDE)
						TURNO = 2

						#para ver que llegue al final de la linea
						if(fila_destino == 7):
							TURNO = 3
					else:
						grid[fila_inicio][columna_inicio] = 1
				else:
					grid[fila_inicio][columna_inicio] = 1
				ficha_seleccionada = [0,(0,0)]
				PUSH = 0

			#ROJAS
			elif (TURNO == 2):
				nivel = 8 #por defecto entre 3 y 7 para que sea algo rapido y no profundice mucho
				
				#para saber la posicion de todas las fichas ROJAS
				rojo = setear_fichas(grid,FICHA_ROJO)
				
				#condicion para saber si mapeo todo
				if(len(rojo)!=0 or TURNO == 3):
					#crear un arbol con matriz, la profundidad y la ficha a hacer
					treeAB = CrearArbol(grid,nivel,FICHA_ROJO)


					# primero se generan el subarbol de jugadas,
					# y setea el valor de cada nodo como la diferencia de cantidad de piezas
					hijos = treeAB.ejecutarAnchoNodos(treeAB,1,nivel)
					# poda buscando los mejores valores para cada nodo y genera la ruta
					podaAB(treeAB,INFINITO_NEGATIVO,INFINITO_POSITIVO)
					jugada = treeAB.rutaAB(treeAB,[])

					nodo = jugada[0]

					inicio = nodo.nodo
					fin = nodo.nodo_fin

					mover_ficha(grid,inicio,fin,FICHA_ROJO)
					grid[inicio[0]][inicio[1]] = 3
					TURNO = 1
					if(fin[0] == 0):
						TURNO = 4

				
		# Establecemos el fondo de pantalla.
		pantalla.fill(NEGRO)
		verde = setear_fichas(grid,FICHA_VERDE)
		rojo = setear_fichas(grid,FICHA_ROJO)
		if(len(verde)==0 or TURNO == 4):
			text_jugada(pantalla,"Ganador ROJO",30,420)
		elif(len(rojo)==0 or TURNO == 3):
			text_jugada(pantalla,"Ganador VERDE",30,420)
		#Textos 
		# if(TURNO==1):
		# 	text_jugada(pantalla," "+J1,200,420)
		# else:
		# 	text_jugada(pantalla," "+J2,200,420)
		#Grid
		for fila in range(tam):
			for columna in range(tam):
				if(fila%2==0):
					if(columna%2==0):
						color = BLANCO
					else:
						color = NEGRO
				else:
					if(columna%2==0):
						color = NEGRO
					else:
						color = BLANCO
				xRect = (MARGEN+LARGO) * columna + MARGEN + xGrid
				yRect = (MARGEN+ALTO) * fila + MARGEN + yGrid
				if (xRect < heightGrid and yRect < widthGrid):
					pygame.draw.rect(pantalla,color, [xRect, yRect, LARGO, ALTO])
				if(grid[fila][columna]==1):
					pygame.draw.circle(pantalla,VERDE,(xRect+SALTO/2,yRect+SALTO/2),ALTO/2)
				elif(grid[fila][columna]==2):
					pygame.draw.circle(pantalla,ROJO,(xRect+SALTO/2,yRect+SALTO/2),ALTO/2)
				if (ficha_seleccionada[0]==FICHA_VERDE):
					x_rect = (MARGEN+LARGO) * ficha_seleccionada[1][1] + MARGEN + xGrid
					y_rect = (MARGEN+ALTO) * ficha_seleccionada[1][0] + MARGEN + yGrid
					pygame.draw.circle(pantalla,NEGRO,(x_rect+SALTO/2,y_rect+SALTO/2),ALTO/2,1)
				elif(ficha_seleccionada[0]==FICHA_ROJO):
					x_rect = (MARGEN+LARGO) * ficha_seleccionada[1][1] + MARGEN + xGrid
					y_rect = (MARGEN+ALTO) * ficha_seleccionada[1][0] + MARGEN + yGrid
					pygame.draw.circle(pantalla,ROJO,(x_rect+SALTO/2,y_rect+SALTO/2),ALTO/2,1)
				for element in jugadas:
					x_rect = (MARGEN+LARGO) * element[1] + MARGEN + xGrid
					y_rect = (MARGEN+ALTO) * element[0] + MARGEN + yGrid
					pygame.draw.circle(pantalla,NEGRO,(x_rect+SALTO/2,y_rect+SALTO/2),ALTO/2,1)


		# Limitamos a 20 fotogramas por segundo.
		reloj.tick(50)
		# Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
		pygame.display.flip()

	pygame.quit()

main()

