# Bibliotecas necessárias ao script:
import numpy as np  # importa a biblioteca numpy (que trabalha com arrays numéricos)
import time  # importa a biblioteca utilizada para contar o tempo
import pandas as pd  # biblioteca para trabalhar com data frames
import math  # para funções matemáticas


################################################
# Merge

def merge(array1, array2):
    IndiceLeft = IndiceRight = trocas = comparacoes = 0
    qtd_a1 = len(array1)
    qtd_a2 = len(array2)

    elementos = True
    array_final = []
    while IndiceLeft < qtd_a1 and IndiceRight < qtd_a2:
        if array1[IndiceLeft] <= array2[IndiceRight]:
            array_final.append(array1[IndiceLeft])
            IndiceLeft = IndiceLeft + 1
        else:
            array_final.append(array2[IndiceRight])
            IndiceRight = IndiceRight + 1

    if IndiceRight < qtd_a2 and IndiceLeft >= qtd_a1:  # array 1 terminou
        array_final.extend(array2[IndiceRight:qtd_a2 + 1])

    if IndiceLeft < qtd_a1 and IndiceRight >= qtd_a2:  # array 2 terminou
        array_final.extend(array1[IndiceLeft:qtd_a1 + 1])
    
    print(array_final)

    return array_final  # , {'trocas':trocas, 'comparacoes':comparacoes}


# Recebe uma lista de arrays e intercala-os 2 a 2
# retorna um array com o resultado da intercalação
def two_way_merge(lst_arrays):
    array_resultante = []

    # a implementar pois o seguinte só concatena
    for lst in lst_arrays:
        array_resultante.extend(lst)

    return array_resultante


# Recebe uma lista de arrays e intercala-os usando estrutura similar a heap-min
# retorna um array com o resultado da intercalação
def multi_way_merge(lst_arrays):
    array_resultante = []

    # a implementar pois o seguinte só concatena
    for lst in lst_arrays:
        array_resultante.extend(lst)

    return array_resultante

# MERGE SORT
def merge_sort(array):

    trocas = comparacoes = pos_troca = 0
    
    print('a implementar...')
    Mid = (len(array)) // 2
    Left =  array [:Mid]
    Right = array[Mid:]
    print("array que chamou: ",array)
    print (Left,Right )
    print()
    print (len(Left), len(Right))
    if(len(Left) != 1):
        merge_sort(Left)
    if (len(Right) != 1): 
        merge_sort(Right)
    print("___________________agora juntando_______________________")
    print ("Array left e right : ",Left, Right)
    
    
    # print("array vazio" , array)
    # array= merge(Left,Right) precisa de ponteiros pra isso e o python não tem, não consegui nem com métodos destrutivos
    # print("array que chamou após: ",array)
    IndiceLeft = IndiceArray = IndiceRight = 0
 
    while IndiceLeft < len(Left) and IndiceRight < len(Right):
        if Left[IndiceLeft] <= Right[IndiceRight]:
            array[IndiceArray] = Left[IndiceLeft]
            IndiceLeft += 1
        else:
            array[IndiceArray] = Right[IndiceRight]
            IndiceRight += 1
            IndiceArray += 1
 
        #Se o lado esquerdo acabar, devo colocar no array
    while IndiceLeft < len(Left):
        array[IndiceArray] = Left[IndiceLeft]
        IndiceLeft += 1
        IndiceArray += 1
        #idem ao anterior
    while IndiceRight < len(Right):
        array[IndiceArray] = Right[IndiceRight]
        IndiceRight += 1
        IndiceArray += 1
    print("array trocado:" ,array)
    
        



    return {'trocas': trocas, 'comparacoes': comparacoes}


def heapify(array, N, indice):
    Maior = indice 
    Left = 2 * indice + 1  # left = 2*IndiceLeft + 1
    Right = 2 * indice + 2  # right = 2*IndiceLeft + 2

    # See if left child of root exists and is
    # greater than root
    if Left < N and array[Maior] < array[Left]:
        Maior = Left

    # See if right child of root exists and is
    # greater than root
    if Right < N and array[Maior] < array[Right]:
        Maior = Right

    # Change root, if needed
    if Maior != indice:
        array[indice], array[Maior] = array[Maior], array[indice]  # swap

        # Heapify the root.
        heapify(array, N, Maior)

def heap_sort(array):
    N = len(array)
  
    # Build a maxheap.
    for IndiceLeft in range(N//2 - 1, -1, -1):
        heapify(array, N, Indice)
  
    
    for Indice in range(N-1, 0, -1):
        array[Indice], array[0] = array[0], array[Indice]  
        heapify(array, Indice, 0)

def getMAXDigitos(numero):
    resto = numero
    digito = 1
    while resto >= 1:
        resto = resto / 10
        if resto >= 1:
            digito +=1
    return digito
def getDigitos(numero, digito):
    num = numero
    for i in range(digito,1, -1):
        num = num // 10
    while num >= 10:
        num -=10
    return num
       
        

def radix_sort_LSD(array):
    ListaAux = []
    MaiorInt = max(array)
    MaxDigitos = getMAXDigitos(MaiorInt)
    for i in range(1,MaxDigitos+1, 1):
        for j in range(0,len(array),1):
            DigitoValor = getDigitos(array[j],i)
            print ("Digito da posicao" ,i-1, "Do elemento:", array[j])
            print(DigitoValor)
            for k in range(0,len(array)-1, 1):
                if DigitoValor < getDigitos(array[k],i):
                    array[j], array[k] = array[k], array[j]
                    


      
    # print(MaxDigitos) 
    return array

def counting_sort(array):
    ArrayAuxiliar = [0 for i in range(30)]
    ArraySaida = [0 for i in range(len(array) +5)]
    for j in range(0,len(array),1):
        ArrayAuxiliar[array[j]] += 1
        
    for i in range(1, len(ArrayAuxiliar)-1,1):
        ArrayAuxiliar[i+1] = ArrayAuxiliar[i]+ ArrayAuxiliar[i+1]
    for k in range(0,len(array),1):
        ArraySaida[ArrayAuxiliar[array[k]]-1] = array[k]
        ArrayAuxiliar[array[k]] -=1
        print("Auxiliar:",ArrayAuxiliar)
        print()
        print("Saida: ",ArraySaida)
        
    return ArraySaida

array = [1,7,10,1,28]
# array = radix_sort_LSD(array)
print (array)
counting_sort(array)

# merge_sort(array)
# print(array)


