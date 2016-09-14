from defines import *
from tablero import *
from juego import *
from arbol import *

import random
import sys


def setear_fichas(matriz,ficha):
	#setear donde se encuentran todas las fichas actuales
	lista = []
	for x in range(len(matriz)):
			for y in range(len(matriz[x])):
				if (matriz[x][y] == ficha):
					lista.append((x,y))
	return lista


def podaAB(tree,alfa,beta):
	tree.setAB(alfa,beta)
	dth = tree.depth(tree)
	
	for son in tree.sons:
		val = podaAB(son,tree.alfa,tree.beta)
		if(dth%2==0):#MINIMOS beta pares
			if(tree.beta>=val):
				tree.beta=val
				tree.valor=val
				tree.ruta = son
		else: #MAXIMOS alfa impares
			if(tree.alfa<=val):
				tree.alfa = val
				tree.valor= val
				tree.ruta = son
	return tree.valor

def CrearArbol(matriz,nivel,tipo):
	grid = matriz
	#construir el arbol con la matriz, pos inicial, pos final y tipo de ficha
	treeAB = Tree(grid,(0,0),(0,0),tipo)
	contador = 1
	padre = (0,0)
	# Creamos el primer nivel
	fichas = setear_fichas(grid,tipo)
	for ficha in fichas:
		#seteamos todas las jugadas que hara para la maquina
		jugadas = posibles_jugadas(grid,ficha,tipo)
		for jugada in jugadas:
			# print jugada,
			treeAB.addNodo(treeAB,padre,ficha,jugada,tipo)

	#retorna una cola con todos los hijos de la raiz en el nivel 1
	act = treeAB.ejecutarAnchoNodos(treeAB,1,contador+1)
	for hijo in act:
		#actualiza nodo
		hijo.actualizarNodo()

	contador+=1
	while(contador<nivel):
		padres = treeAB.ejecutarAncho(treeAB,1,contador)
		nodos = treeAB.ejecutarAnchoNodos(treeAB,1,contador)
		if(contador%2==0):
			for padre in range(len(padres)):
				nodo = nodos[padre]
				fichas = setear_fichas(nodo.matriz,FICHA_VERDE)
				for ficha in fichas:
					jugadas = posibles_jugadas(nodo.matriz,ficha,FICHA_VERDE)
					for jugada in jugadas:
						nodo.addNodo(nodo,nodo.nodo,ficha,jugada,FICHA_VERDE)
			act = treeAB.ejecutarAnchoNodos(treeAB,1,contador+1)
			for hijo in act:
				hijo.actualizarNodo()
			contador+=1
		else:
			for padre in range(len(padres)):
				nodo = nodos[padre]
				fichas = setear_fichas(nodo.matriz,FICHA_ROJO)
				for ficha in fichas:
					jugadas = posibles_jugadas(nodo.matriz,ficha,FICHA_ROJO)
					for jugada in jugadas:
						nodo.addNodo(nodo,nodo.nodo,ficha,jugada,FICHA_ROJO)
			act = treeAB.ejecutarAnchoNodos(treeAB,1,contador+1)
			for hijo in act:
				hijo.actualizarNodo()
			contador+=1
	nodos = treeAB.ejecutarAnchoNodos(treeAB,1,contador)
	if(contador%2==0):
		for nodo in nodos:
			if(nodo.nodo_fin[0]==0):
				nodo.setValor(100)
			else:
				nodo.setValor(len(setear_fichas(nodo.matriz,FICHA_VERDE)) - len(setear_fichas(nodo.matriz,FICHA_ROJO)))
				
	else:
		for nodo in nodos:
			if(nodo.nodo_fin[0]==7):
				nodo.setValor(-100)
			else:
				nodo.setValor(len(setear_fichas(nodo.matriz,FICHA_ROJO)) - len(setear_fichas(nodo.matriz,FICHA_VERDE)))
	return treeAB


# MAX = jugada enemiga = len de mis fichas - len de sus fichas
# MIN = jugada mia = len de sus fichas - len de mis fichas
""" 
1 jugada inicial	 MAX
2 jugada mia 		MIN
3 jugada enemiga     MAX
4 jugada mia 		MIN
5 jugada enemiga     MAX
"""
