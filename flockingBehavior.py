import pygame, os, math, time, random
from pygame.locals import *
pygame.init()

# configurar ANCHO y LARGO de la pantalla
ANCHO = 1000 #1000
LARGO = 700	#1000

CENTROX = ANCHO / 2
CENTROY = LARGO / 2

#Si aumento el numero de NUMDRONES, la velocidad baja y viceversa
NUMDRONES = 20

POSPROPAGACION = 10000
VELPROPAGACION = 1
MAXVEL = 3

FRONTERA = 100
LIDERFRONTERA = 200
FRONTERAVELCAMBIO = 0.2

MINDIST = 5.0
MATCHVELWINDOW = 40.0

LIDERDRONERANDOMVELCAMBIO = 0.2
LIDERMAXVEL = 5.0


obstaculos = [[450,500],[475,500],[500,500],[525,500],[625,500],[650,500],[675,500],[700,500],[400,500],[425,500],[400,525],[400,550],[400,650],[400,675],[400,700],[375,700],[350,700],[325,700],[300,700],[275,700],[250,700],[800,200],[250,700],[100,100]]
# obstaculos = [[700,500],[400,500],[425,500],[400,525],[400,550],[400,650],[400,675],[400,700],[375,700],[350,700],[325,700],[300,700],[275,700],[250,700],[800,200],[250,700],[100,100]]
objetivos = [[150,400],[180,400],[210,400],[500,130],[500,100],[500,70],[905,400],[905,430],[905,460]]
RADIOOBSTACULO = 50
RADIOOBJETIVO = 50



tamano = [ANCHO, LARGO]
screen = pygame.display.set_mode(tamano)

# Esto hace que el puntero normal del raton sea invisible en la ventana de graficos
pygame.mouse.set_visible(0)

dronelist = []

feromonaInicial=[]

feromonasDronesNoLider=[]

# Generar lider drone 1

listDroneLideres=[]


liderdronex = 300.0
liderdroney = 300.0
liderdronevx = 5.0
liderdronevy = 0.0

nuevoLider=[liderdronex,liderdroney,liderdronevx,liderdronevy]
listDroneLideres.append(nuevoLider)


# liderdronex2 = 800.0
# liderdroney2 = 700.0
# liderdronevx2 = 5.0
# liderdronevy2 = 0.0

# nuevoLider2=[liderdronex2,liderdroney2,liderdronevx2,liderdronevy2]
# listDroneLideres.append(nuevoLider2)


# liderdronex2 = 100.0
# liderdroney2 = 400.0
# liderdronevx2 = 2.0
# liderdronevy2 = 0.0

# nuevoLider2=[liderdronex2,liderdroney2,liderdronevx2,liderdronevy2]
# listDroneLideres.append(nuevoLider2)

# liderdronex2 = 0.0
# liderdroney2 = 0.0
# liderdronevx2 = 2.0
# liderdronevy2 = 0.0

# nuevoLider2=[liderdronex2,liderdroney2,liderdronevx2,liderdronevy2]
# listDroneLideres.append(nuevoLider2)




# Generar lider drone 2
 


# Generar drones
i = 0

while (i < NUMDRONES):
	x = random.uniform(CENTROX - POSPROPAGACION, CENTROX + POSPROPAGACION)
	y = random.uniform(CENTROY - POSPROPAGACION, CENTROY + POSPROPAGACION)
	vx = random.uniform(-VELPROPAGACION, VELPROPAGACION)
	vy = random.uniform(-VELPROPAGACION, VELPROPAGACION)
	
	nuevodrone = [x, y, vx, vy]

	dronelist.append(nuevodrone)
	i += 1


contadorObjetivo1=0
contadorObjetivo2=0
contadorObjetivo3=0

contadorList=[]
contadorList.append(contadorObjetivo1)
contadorList.append(contadorObjetivo2)
contadorList.append(contadorObjetivo3)


while(1):
	screen.fill((0,0,0))
	for lider in listDroneLideres:
		# Actualizar lider drone posicion and propagacion
		if (lider[0] < LIDERFRONTERA):
			lider[2]  += FRONTERAVELCAMBIO
		if (lider[1]  < LIDERFRONTERA):
			lider[3]  += FRONTERAVELCAMBIO
		if (lider[0] > ANCHO - LIDERFRONTERA):
			lider[2] -= FRONTERAVELCAMBIO
		if (lider[1] > LARGO - LIDERFRONTERA):
			lider[3] -= FRONTERAVELCAMBIO


		# Graficar liderdrone y actualizar
		pygame.draw.circle(screen, (255,0,255), (int(lider[0]), int(lider[1])), 5, 0)
		lider[2] += random.uniform(-LIDERDRONERANDOMVELCAMBIO, LIDERDRONERANDOMVELCAMBIO)
		lider[3] += random.uniform(-LIDERDRONERANDOMVELCAMBIO, LIDERDRONERANDOMVELCAMBIO)

		# maxima vel
		velocidad = math.sqrt(lider[2]*lider[2] + lider[3]*lider[3])
		if (velocidad > LIDERMAXVEL):
			lider[2] = lider[2] * LIDERMAXVEL/velocidad
			lider[3] = lider[3] * LIDERMAXVEL/velocidad

		lider[0] += lider[2]
		lider[1] += lider[3]

		# graficar drones, posiciones and velocidad
		i = 0
		while (i < NUMDRONES):

			# Hacer copias para mayor claridad
			x = dronelist[i][0]
			y = dronelist[i][1]
			vx = dronelist[i][2]
			vy = dronelist[i][3]

			# los colores 
			colr = int(float(i) * 255.0/NUMDRONES)
			colg = int((NUMDRONES-float(i)) * 255.0/NUMDRONES)
			colb = 255
			
			pygame.draw.circle(screen, (255,255,0), (int(x), int(y)), 2, 0)

			# drones se alejan de la frontera
			if (x < FRONTERA):
				vx += FRONTERAVELCAMBIO
			if (y < FRONTERA):
				vy += FRONTERAVELCAMBIO
			if (x > ANCHO - FRONTERA):
				vx -= FRONTERAVELCAMBIO
			if (y > LARGO - FRONTERA):
				vy -= FRONTERAVELCAMBIO

			# drones se mueven hacia el drone lider
			liderdiffx = lider[0] - x
			liderdiffy = lider[1] - y
			vx += 0.007 * liderdiffx
			vy += 0.007 * liderdiffy

			# Alejarse de otros drones cercanos
			# Tambien calcular la velocidad media de los drones en la ventana
			j = 0
			# Para calcular la velocidad media de otros drones
			avxtotal = 0
			avytotal = 0
			avcount = 0
			while (j < NUMDRONES):
				if (j != i):
					dx = dronelist[j][0] - x
					dy = dronelist[j][1] - y
					dist = math.sqrt(dx*dx + dy*dy)
					if (dist < MINDIST):
						vx -= dx * 0.2
						vy -= dy * 0.2
					if (dist < MATCHVELWINDOW):
						avxtotal += dronelist[j][2]
						avytotal += dronelist[j][3]
						avcount += 1
				j += 1
			# Corresponde a la velocidad media de los drones cercanos
			if (avcount != 0):
				avx = avxtotal / avcount
				avy = avytotal / avcount
				vx = 0.9 * vx + 0.1 * avx
				vy = 0.9 * vy + 0.1 * avy

			# Rebote de obstaculos y bajar la velocidad
			for obstaculo in obstaculos:
				dx = obstaculo[0] - x
				_liderdronedx=obstaculo[0] - lider[0]
				dy = obstaculo[1] - y
				_liderdronedy=obstaculo[1] - lider[1]
				dist = math.sqrt(dx*dx + dy*dy)
				dist1 = math.sqrt(_liderdronedx*_liderdronedx + _liderdronedy*_liderdronedy)
				

				if (dist < RADIOOBSTACULO):
					vx -= dx * 0.1
					vx *= 0.6
					vy -= dy * 0.1
					vy *= 0.6

				if (dist1 < RADIOOBSTACULO):
					# pygame.draw.circle(screen, (255,255,255), (int(lider[0]), int(lider[1])), 60, 0)
					lider[2]-=_liderdronedx*0.1
					lider[2]*=0.6
					lider[3]-=_liderdronedy*0.1
					lider[3]*=0.6				

			#busqueda de objetivos		
			for obj in objetivos:
				dx = obj[0] - x
				_liderdronedx=obj[0] - lider[0]
				dy = obj[1] - y
				_liderdronedy=obj[1] - lider[1]
				dist = math.sqrt(dx*dx + dy*dy)
				dist1 = math.sqrt(_liderdronedx*_liderdronedx + _liderdronedy*_liderdronedy)


				if ((dist < RADIOOBJETIVO) ):
					# pygame.draw.circle(screen, (255,255,255), (int(lider[0]), int(lider[1])), 30, 0)
					posxFer=(x)
					posyFer=(y)
					nuevoferomonaNoDroneInicial = [posxFer, posyFer]
					feromonasDronesNoLider.append(nuevoferomonaNoDroneInicial)
					numero = (objetivos.index(obj))
					if (numero<3):
						contadorList[0]+=0.025
					if ((numero>=3) and (numero<6)):
						contadorList[1]+=0.025
					if (numero>=6):
						contadorList[2]+=0.025


				if ((dist1 < RADIOOBJETIVO + 15) ):
					# pygame.draw.circle(screen, (255,255,255), (int(lider[0]), int(lider[1])), 30, 0)
					posxFer=(lider[0])
					posyFer=(lider[1])
					nuevoferomonaInicial = [posxFer, posyFer]
					feromonaInicial.append(nuevoferomonaInicial)
					numero = (objetivos.index(obj))
					if (numero<3):
						contadorList[0]+=0.025
					if ((numero>=3) and (numero<6)):
						contadorList[1]+=0.025
					if (numero>=6):
						contadorList[2]+=0.025

					
			# velocidad maxima
			velocidad = math.sqrt(vx*vx + vy*vy)
			if (velocidad > MAXVEL):
				vx = vx * MAXVEL/velocidad
				vy = vy * MAXVEL/velocidad

			# actualizar posiciones de acuerdo a velocidad
			dronelist[i][0] += vx
			dronelist[i][1] += vy
			dronelist[i][2] = vx
			dronelist[i][3] = vy
			i += 1

	for obstaculo in obstaculos:
		pygame.draw.rect(screen, (255,0,0), (int(obstaculo[0]), int(obstaculo[1]),RADIOOBSTACULO,RADIOOBSTACULO), 0)

	for obj in objetivos:
		pygame.draw.circle(screen, (0,100,0), (int(obj[0]), int(obj[1])), RADIOOBJETIVO, 28)

	for fer in feromonaInicial:
		pygame.draw.circle(screen, (255,255,255), (int(fer[0]), int(fer[1])), 10, 0)

	for fer in feromonasDronesNoLider:
		pygame.draw.circle(screen, (0,191,255), (int(fer[0]), int(fer[1])), 1, 0)

	#time.sleep(0.1)
	pygame.display.flip()
	print("contador 1 es : ", int(contadorList[0]), "contador 2 es : ", int(contadorList[1]),"contador 3 es : ", int(contadorList[2]))
i += 1