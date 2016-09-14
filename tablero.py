import pygame
from defines import *
from math import sqrt


def crear_tablero():
    if (tam == 10):
        # grid = [[0,1,0,1,0,1,0,1,0,1],
        #         [1,0,1,0,1,0,1,0,1,0],
        #         [0,1,0,1,0,1,0,1,0,1],
        #         [1,0,1,0,1,0,1,0,1,0],
        #         [0,3,0,3,0,3,0,3,0,3],
        #         [3,0,3,0,3,0,3,0,3,0],
        #         [0,2,0,2,0,2,0,2,0,2],
        #         [2,0,2,0,2,0,2,0,2,0],
        #         [0,2,0,2,0,2,0,2,0,2],
        #         [2,0,2,0,2,0,2,0,2,0]]


        
		grid = [[0,1,0,1,0,1,0,1,0,1],
                [1,0,1,0,1,0,1,0,1,0],
                [0,3,0,3,0,3,0,3,0,3],
                [3,0,3,0,3,0,3,0,3,0],
                [0,3,0,3,0,3,0,3,0,3],
                [3,0,3,0,3,0,3,0,3,0],
                [0,3,0,3,0,3,0,3,0,3],
                [3,0,3,0,3,0,3,0,3,0],
                [0,2,0,2,0,2,0,2,0,2],
                [2,0,2,0,2,0,2,0,2,0]]
    # elif(tam == 8):
    #     grid = [[0,1,0,1,0,1,0,1],
    #             [1,0,1,0,1,0,1,0],
    #             [0,1,0,1,0,1,0,1],
    #             [3,0,3,0,3,0,3,0],
    #             [0,3,0,3,0,3,0,3],
    #             [2,0,2,0,2,0,2,0],
    #             [0,2,0,2,0,2,0,2],
    #             [2,0,2,0,2,0,2,0]]

    elif(tam == 8):
        grid = [[0,1,0,1,0,1,0,1],
                [1,0,1,0,1,0,1,0],
                [0,3,0,3,0,3,0,3],
                [3,0,3,0,3,0,3,0],
                [0,3,0,3,0,3,0,3],
                [3,0,3,0,3,0,3,0],
                [0,2,0,2,0,2,0,2],
                [2,0,2,0,2,0,2,0]]
                
    elif(tam == 6):
        grid = [[0,1,0,1,0,1],
                [1,0,1,0,1,0],
                [0,3,0,3,0,3],
                [3,0,3,0,3,0],
                [0,2,0,2,0,2],
                [2,0,2,0,2,0]]

    return grid

def encontadorrar_centro(tupla):
    x = (tupla[1]*(LARGO + MARGEN)+xGrid)+LARGO/2
    y = (tupla[0]*(LARGO + MARGEN)+yGrid)+ALTO/2
    return (x,y)

def distan_eucli(first,second):
	return sqrt(sum( (second - first)**2 for first, second in zip(first, second)))

def index_grafo(grafo,punto_actual):
    for index in range(len(grafo)):
        if(punto_actual == grafo[index].pos):
            return index

def text_jugada(pantalla,jugada,x,y):
    myfont = pygame.font.SysFont("monospace", 15)
    text=myfont.render(jugada, 1,ROJO)
    pantalla.blit(text, (x, y))
