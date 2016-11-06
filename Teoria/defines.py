NEGRO = (0, 0, 0) # en vez de negro para el Fondo sera amarillo
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)
BEIGE = (255, 255, 255) # en vez de beige para el tablero sera blanco
MARRON = (0, 0, 0) # en vez de marron sera negro
BEIGE_OSCURO = (0, 100, 0)
NEGRO_CLARO = (255, 0, 0) #en vez de negro claro sera rojo 

#Botones
LEFT = 1
RIGHT = 3
#Pantalla
width = 350#420
height = 340#450#600
# Establecemos el margen entre las celdas.
MARGEN = 1
#Margen de grid
xGrid = 20
yGrid = 20
widthGrid = 300#400#560
heightGrid = 290#390#550
#numero de bloques
tam = 6
#Largo y alto de los bloques
LARGO = (widthGrid/tam)- 3*MARGEN
ALTO = (heightGrid/tam)- 1*MARGEN
#Fichas
FICHAS_BEIGE = 10
FICHAS_NEGRO = 10
# FICHA_BEIGE = 1
FICHA_VERDE =1
# FICHA_NEGRO = 2
FICHA_ROJO = 2
VACIO = 3
#Espacio entre puntos
SALTO = ((MARGEN+LARGO)*2 +MARGEN + xGrid)-((MARGEN+LARGO) +MARGEN + xGrid)
#Juego 
TURNO = 1
#Nombre de los jugadores
J1 = "JUGADOR  # 1 (VERDES)"
J2 = "JUGADOR  # 2 (ROJAS)"
#Niveles	
EASY = 2
MEDIUM = 4
HARD = 8
#INFINITOS
INFINITO_NEGATIVO = -10000
INFINITO_POSITIVO =  10000