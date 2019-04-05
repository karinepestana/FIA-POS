import numpy as np
from random import randint
import time
import argparse

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

if __name__ == '__main__':
    #Le a dimensao (nxn) do jogo
    ap = argparse.ArgumentParser()
    ap.add_argument('-d', "--dimensao", required=True, help="Informe o valor da matriz quadrada para o jogo")
    ap.add_argument('-n', "--vezes", required=True, help="Informe o valor de vezes que a matriz será embaralhada")
    args = vars(ap.parse_args())    
    #dimension = int(args["dimensao"])
    size = int(args["dimensao"])
    n = int(args["vezes"])

    m = np.arange(1, size*size+1, 1).reshape(size, size)
    m[size-1,size-1] = 0

    for x in range(0, n):
        embaralha(m)

    ref_arquivo = open("matriz.txt",'w')
    ref_arquivo.write(str(m))
    ref_arquivo.close()