import numpy as np
from random import randint
import time
import argparse

class Node:
	def __init__(self, data):
        
		self.nodo_pai = None
		self.direita = None
		self.esquerda = None
		self.cima = None
		self.baixo = None
		self.data = data
		self.i = 0
		self.j = 0
        
	def insert(self, data):
		if self.direita is None:
			self.direita = Node(data)            
		elif self.esquerda is None:
			self.esquerda = Node(data)
		elif self.cima is None:
			self.cima = Node(data)
		elif self.baixo is None:
			self.baixo = Node(data)

def abre_no(raiz):
	rs, v = movimento(raiz)
	for i in range (0,v):
		rs[i].nodo_pai = raiz
		raiz.insert(rs[i].data)        
	lista_dados.extend(rs)          

def busca_zero(m):
	i= 0
	j= 0
	while (i<size) and (m[i,j]!= 0):
		while (j<size) and (m[i,j]!= 0):
			j=j+1
		if j!=size and m[i,j]==0:
			break
		else:
			j=0
			i=i+1
        
	if i >= size:
		i = size-1
	if j >= size:
		j = size-1
 
	return i,j

def movimento(m):
	i = m.i
	j = m.j
	saidas = []
	cont = 0
	v = 0

	for count in range (0,4):
		m_aux = m.data.copy()
		if count == 0:
			if j+1 <= size-1:
				aux = m_aux[i,j+1]
				m_aux[i,j+1] = 0
				m_aux[i,j] = aux
				#print(m_aux)
				m_aux = Node(m_aux)
				m_aux.i = i
				m_aux.j = j+1
				saidas.append(m_aux)
				m_aux = [] 
				v = v +1
		elif count == 1:
			if j-1 >= 0:
				aux = m_aux[i, j-1]
				m_aux[i, j-1] = 0
				m_aux[i,j] = aux
				#print(m_aux)
				m_aux = Node(m_aux)
				m_aux.i = i
				m_aux.j = j-1
				saidas.append(m_aux)
				m_aux = [] 
				v = v +1	
		elif count == 2:
			if i+1 <= size-1:
				aux = m_aux[i+1,j]
				m_aux[i+1,j] = 0
				m_aux[i,j] = aux
				#print(m_aux)
				m_aux = Node(m_aux)
				m_aux.i = i+1
				m_aux.j = j
				saidas.append(m_aux)
				m_aux = [] 
				v = v +1	
		elif count == 3:
			if i-1 >= 0:
				aux = m_aux[i-1, j]
				m_aux[i-1, j] = 0
				m_aux[i,j] = aux
				#print(m_aux)
				m_aux = Node(m_aux)
				m_aux.i = i-1
				m_aux.j = j
				saidas.append(m_aux)
				m_aux = [] 	
				v = v +1
            
	return saidas,v

def acceptable_runtime(start_time, nodos):
		
		if time.time()-start_time >= 3600:
			print("\nBusca por aprofundamento iterativo\n")
			print("Situação: Busca não encontrou solução")
			print("Nós abertos: " + str(nodos))
			hour, minutes, seconds = 0, 0, 0
			end_time = time.time() - ini
			hour = end_time // 3600
			end_time %= 3600
			minutes = end_time // 60
			end_time %= 60
			seconds = end_time
			print("Tempo de execução: %d"  %hour ,"horas, %d" %minutes, "minutos e %.2f segundos" % seconds)
			return False
		return True
	

if __name__ == '__main__':
	#Le a dimensao (nxn) do jogo
	ap = argparse.ArgumentParser()
	ap.add_argument('-d', "--dimensao", required=True, help="Informe o valor da matriz quadrada para o jogo")
	args = vars(ap.parse_args())	
	#dimension = int(args["dimensao"])
	size = int(args["dimensao"])

	ini = time.time()
	#size = 3
	m = np.arange(1, size*size+1, 1).reshape(size, size)
	m[size-1,size-1] = 0
	saida_esperada = m.copy()

	#for x in range(0, 4):
		#embaralha(m)

	ref_arquivo = open("matriz.txt",'r')
	linha = ref_arquivo.readline()
	valores = []
	m = np.arange(0, size*size, 1)
	i = 0

	while linha:
		valores = linha.split()
		m[i] = (int(valores[0][-1:]))
		m[i+1] = (int(valores[1][-1:]))
		if i+2 == 8:
			m[i+2] = int(valores[2][:-2])
		else:
			m[i+2] = int(valores[2][:-1])
		linha = ref_arquivo.readline()
		i = i+3

	ref_arquivo.close()
	m = m.reshape(size, size)
	#print(type(m))

	#print(type(m))
	solucao_encontrada = False
	nos_abertos = 0

	lista_dados = list()
	nodo_inicial = Node(m)
	a, b = busca_zero(m)
	nodo_inicial.i = a
	nodo_inicial.j = b
	lista_dados.append(nodo_inicial)
	matriz_embaralhada = m.copy()
	nos_abertos = nos_abertos +1

	matriz = None
	limite = 1
	while solucao_encontrada == False and acceptable_runtime(ini, nos_abertos):
		lista_dados = list()
		lista_dados.append(Node(m))
		matriz_embaralhada = m.copy()
		for i in range(0,limite):
			matriz = lista_dados.pop(0)
			nos_abertos = nos_abertos +1

			if not np.array_equal(matriz.data,saida_esperada):
				abre_no(matriz)
			else:
				solucao_encontrada = True
				break
			limite = limite +1


	if solucao_encontrada:
		print("\nBusca por aprofundamento iterativo\n")
		print("Situação: Busca encontrou solução")
		print("Nós abertos: " + str(nos_abertos))
		hour, minutes, seconds = 0, 0, 0
		end_time = time.time() - ini
		hour = end_time // 3600
		end_time %= 3600
		minutes = end_time // 60
		end_time %= 60
		seconds = end_time
		print("Tempo de execução: %d"  %hour ,"horas, %d" %minutes, "minutos e %.2f segundos" % seconds)
		print("Caminho para encontrar a solução: ")
		caminho = list()
		count = 0
	    
		while matriz != None:
			caminho.append(matriz.data)
			matriz = matriz.nodo_pai
			count = count +1
	        
		caminho.reverse()

		for i in range(0, count):
			print(caminho[i])
	    #print(caminho)
	