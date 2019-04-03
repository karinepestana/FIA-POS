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
		lista_dados.insert(0, rs[i])          

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
        
            
    #Verifica se o 0 está nos cantos(0) ou nas bordas(1) ou no meio(2)
        
	if (i == 0):
		aux = 1
		if (j == 0) or (j == size-1):
			s = 0
		else:
			s = 1
	elif i == size-1:
		if (j == 0) or (j == size-1):
			s = 0
		else:
			s = 1
	elif (j == 0) or (j == size-1):
		s = 1
	else:
		s = 2           
        
	return i,j,s

def embaralha(m):
	i,j,s = busca_zero(m)
    #print(i, j, s)
    #print(m)
    
	if s == 0:
		rand = randint(0,1)
		if rand == 0:
			if j == 0:
				aux = m[i,j+1]
				m[i,j+1] = 0
				m[i,j] = aux
			else:
				aux = m[i, j-1]
				m[i, j-1] = 0
				m[i,j] = aux
		else:
			if i == 0:
				aux = m[i+1,j]
				m[i+1,j] = 0
				m[i,j] = aux
			else:
				aux = m[i-1, j]
				m[i-1, j] = 0
				m[i,j] = aux 
	elif s == 1:
		rand = randint(0,2)
		if rand == 0:
			if i == 0 or i == size-1:
                #borda superior ou inferior -> troca com o da direita
				aux = m[i,j+1]
				m[i,j+1] = 0
				m[i,j] = aux
			else:
                #borda lateral -> troca com o de baixo
				aux = m[i+1,j]
				m[i+1,j] = 0
				m[i,j] = aux
		elif rand == 1:
			if i == 0 or i == size-1:
                #borda superior ou inferior -> troca com o da esquerda
				aux = m[i, j-1]
				m[i, j-1] = 0
				m[i,j] = aux
			else:
                #borda lateral -> troca com o de cima
                #print(m)
                #print(i,j,s)
				aux = m[i-1, j]
				m[i-1, j] = 0
				m[i,j] = aux
		else:
			if i == 0:
                #borda superior -> troca com o de baixo
				aux = m[i+1,j]
				m[i+1,j] = 0
				m[i,j] = aux
			elif i == size-1:
                #borda inferior -> troca com o de cima
				aux = m[i-1, j]
				m[i-1, j] = 0
				m[i,j] = aux
			elif j == 0:
                #borda lateral esquerda -> troca com o do lado direito
                #print(m)
                #print(i,j,s)
				aux = m[i,j+1]
				m[i,j+1] = 0
				m[i,j] = aux
			else:
                #borda lateral direita -> troca com o do lado esquerdo
				aux = m[i, j-1]
				m[i, j-1] = 0
				m[i,j] = aux
	else:
		rand = randint(0,3)
		if rand == 0:
			aux = m[i,j+1]
			m[i,j+1] = 0
			m[i,j] = aux
		elif rand == 1:
			aux = m[i, j-1]
			m[i, j-1] = 0
			m[i,j] = aux
		elif rand == 2:
			aux = m[i+1,j]
			m[i+1,j] = 0
			m[i,j] = aux
		else:
			aux = m[i-1, j]
			m[i-1, j] = 0
			m[i,j] = aux
            
	return m

def movimento(m):
	i,j,s = busca_zero(m.data)
	saidas = []
	cont = 0
	v = 0
   
	if s == 0:   
		cont = 0
		v = 2
		for cont in range (0,2):            
			m_aux = m.data.copy()
			if cont == 0:
				if j == 0:
					aux = m_aux[i,j+1]
					m_aux[i,j+1] = 0
					m_aux[i,j] = aux
				else:
					aux = m_aux[i, j-1]
					m_aux[i, j-1] = 0
					m_aux[i,j] = aux
                #print("s = 0 cont = 0")
                #print(m_aux)
                #print(" ")
			else:
				if i == 0:
					aux = m_aux[i+1,j]
					m_aux[i+1,j] = 0
					m_aux[i,j] = aux
				else:
					aux = m_aux[i-1, j]
					m_aux[i-1, j] = 0
					m_aux[i,j] = aux
                #print("s = 0 cont = 1")
                #print(m_aux)
                #print(" ")
			m_aux = Node(m_aux)
			saidas.append(m_aux)
			m_aux = []            
            
	elif s == 1:
        
		cont = 0
		v = 3
		for cont in range (0,3):
			m_aux = m.data.copy()
			if cont == 0:
				if i == 0 or i == size-1:
                    #borda superior ou inferior -> troca com_aux o da direita
					aux = m_aux[i,j+1]
					m_aux[i,j+1] = 0
					m_aux[i,j] = aux
				else:
                    #borda lateral -> troca com_aux o de baixo
					aux = m_aux[i+1,j]
					m_aux[i+1,j] = 0
					m_aux[i,j] = aux
                #print("s = 1 cont = 0")
                #print(m_aux)
                #print(" ")
			elif cont == 1:
				if i == 0 or i == size-1:
                    #borda superior ou inferior -> troca com_aux o da esquerda
					aux = m_aux[i, j-1]
					m_aux[i, j-1] = 0
					m_aux[i,j] = aux
				else:
                    #borda lateral -> troca com_aux o de cim_auxa
                    #print(m_aux)
                    #print(i,j,s)
					aux = m_aux[i-1, j]
					m_aux[i-1, j] = 0
					m_aux[i,j] = aux
                #print("s = 1 cont = 1")
                #print(m_aux)
                #print(" ")
			else:
				if i == 0:
                    #borda superior -> troca com_aux o de baixo
					aux = m_aux[i+1,j]
					m_aux[i+1,j] = 0
					m_aux[i,j] = aux
				elif i == size-1:
                    #borda inferior -> troca com_aux o de cim_auxa
					aux = m_aux[i-1, j]
					m_aux[i-1, j] = 0
					m_aux[i,j] = aux
				elif j == 0:
                    #borda lateral esquerda -> troca com_aux o do lado direito
                    #print(m_aux)
                    #print(i,j,s)
					aux = m_aux[i,j+1]
					m_aux[i,j+1] = 0
					m_aux[i,j] = aux
				else:
                    #borda lateral direita -> troca com_aux o do lado esquerdo
					aux = m_aux[i, j-1]
					m_aux[i, j-1] = 0
					m_aux[i,j] = aux
                #print("s = 1 cont = 2")
                #print(m_aux)
                #print(" ")
			m_aux = Node(m_aux)
			saidas.append(m_aux)
			m_aux = []
	else:
		cont = 0
		v = 4
		for cont in range (0,4):
			m_aux = m.data.copy()
			if cont == 0:
				aux = m_aux[i,j+1]
				m_aux[i,j+1] = 0
				m_aux[i,j] = aux
                #print("s = 2 cont = 0")
                #print(m_aux)
                #print(" ")
			elif cont == 1:
				aux = m_aux[i, j-1]
				m_aux[i, j-1] = 0
				m_aux[i,j] = aux
                #print("s = 2 cont = 1")
                #print(m_aux)
                #print(" ")
			elif cont == 2:
				aux = m_aux[i+1,j]
				m_aux[i+1,j] = 0
				m_aux[i,j] = aux
                #print("s = 2 cont = 2")
                #print(m_aux)
                #print(" ")
			else:
				aux = m_aux[i-1, j]
				m_aux[i-1, j] = 0
				m_aux[i,j] = aux
                #print("s = 2 cont = 3")
                #print(m_aux)
                #print(" ")
			m_aux = Node(m_aux)
			saidas.append(m_aux)
			m_aux = []
            
	return saidas, v

def acceptable_runtime(start_time, nodos):
		
		if time.time()-start_time >= 3600:
			print("\nBusca em Profundidade\n")
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

	#for x in range(0, 3):
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

	solucao_encontrada = False
	nos_abertos = 0

	lista_dados = list()
	lista_dados.append(Node(m))
	matriz_embaralhada = m.copy()
	nos_abertos = nos_abertos +1

	matriz = None
	while lista_dados and acceptable_runtime(ini, nos_abertos):
		matriz = lista_dados.pop(0)
		nos_abertos = nos_abertos +1

		if not np.array_equal(matriz.data,saida_esperada):
	 		abre_no(matriz)
		else:
			solucao_encontrada = True
			break


	if solucao_encontrada:
		print("\nBusca em Profundidade\n")
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
	