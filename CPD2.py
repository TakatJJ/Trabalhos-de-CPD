# Bibliotecas necessárias ao script:
import numpy as pd   # importa a biblioteca numpy (que trabalha com arrays numéricos)
import time         # importa a biblioteca utilizada para contar o tempo
import pandas as pd # biblioteca para trabalhar com data frames
import math
import random
################################################
# Algoritmos de ordenação
################################################

# Bubblesort
def bubble_sort(array):
    trocas = comparacoes = pos_troca = 0
    qtd_elementos = len(array)-1
    troca = True
   
    while troca:
        troca = False
        for i in range(0, qtd_elementos):
            comparacoes = comparacoes + 1
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
                troca = True  
                pos_troca = i
                trocas = trocas + 1
        qtd_elementos = pos_troca
               
    return {'trocas':trocas, 'comparacoes':comparacoes}

# Quicksort e funções auxiliares
def quick_sort(array):
    log_operacoes = {'trocas':0, 'comparacoes':0}
    quicksort(array, 0, len(array)-1, log_operacoes)
    return log_operacoes

def quicksort(array, inicio, fim, log_operacoes):
    if fim > inicio:
        pivo = particiona(array, inicio, fim, log_operacoes)
        quicksort(array, inicio, pivo-1, log_operacoes)
        quicksort(array, pivo+1, fim, log_operacoes)
    return log_operacoes

def particiona(array, esquerda, direita, log_operacoes):
    pivo = esquerda
    i = pivo + 1
    j = direita
   
    while i<j:
        while (array[j] >= array[pivo]) and (j > esquerda): # procura menor à direita
            j = j - 1
            log_operacoes['comparacoes'] = log_operacoes['comparacoes'] + 1
       
        while (array[i] < array[pivo]) and (i < direita): # procura maior à esquerda
            log_operacoes['comparacoes'] = log_operacoes['comparacoes'] + 1
            i = i + 1
           
        if (i<j) and (array[i] > array[j]):
            log_operacoes['comparacoes'] = log_operacoes['comparacoes'] + 1
            log_operacoes['trocas'] = log_operacoes['trocas'] + 1
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp

    if array[j] < array[pivo]:
        log_operacoes['comparacoes'] = log_operacoes['comparacoes'] + 1
        log_operacoes['trocas'] = log_operacoes['trocas'] + 1
        tmp = array[j]
        array[j] = array[pivo]
        array[pivo] = tmp
   
    return j;

################################################
# Implementação dos seus algoritmos:
   
def comb_sort(array):
    log_operacoes = {'trocas':0, 'comparacoes':0}
    print('a implementar')
    gap = len(array) - 1
    trocar = 1
    vartemp = 0
    i = 0
    # print(len(array))
    
    # print("\n",)
    while (gap >= 1 or trocar):
        
       
        for i in range(0, len(array) - gap):
            log_operacoes['comparacoes'] += 1
            trocar = 0
            
            if (array[i] > array[i+gap]):
                log_operacoes['trocas'] += 1
                vartemp = array[i]
                array[i] = array[i+gap]
                array[i+gap] = vartemp
                trocar = 1
        gap = int(gap/1.3)
        
               
           
        
       
   
    return log_operacoes
   
def shake_sort(array):
    log_operacoes = {'trocas':0, 'comparacoes':0}
    print('a implementar')
    fim = len(array) - 1
    vartemp = 0
    trocar = 1
    while (trocar == 1):
        trocar = 0
       
        for i in range(0,fim):
            log_operacoes['comparacoes'] +=1
            if array[i] > array[i+1]:
                log_operacoes['trocas'] +=1
                vartemp = array[i]
                array[i] = array[i+1]
                array[i+1] = vartemp
                trocar = 1
    return log_operacoes
   
def quick_sort2(array):
    log_operacoes = {'trocas':0, 'comparacoes':0}
    print('a implementar')
    quicksort2(array, 0, len(array)-1, log_operacoes)
    return log_operacoes
   
def quicksort2(array, inicio, fim, log_operacoes):
    if fim > inicio:
        pivo = particionaRandom(array, inicio, fim, log_operacoes)
        quicksort2(array, inicio, pivo-1, log_operacoes)
        quicksort2(array, pivo+1, fim, log_operacoes)
    return log_operacoes
   
def particionaRandom(array, inicio, fim, log_operacoes):
    pivotrandom = random.randrange(inicio, fim)
    vartemp = 0
   
    vartemp = array[inicio]
    array[inicio] = array[pivotrandom]
    array[pivotrandom] = vartemp
    
    
    return particiona(array, inicio, fim, log_operacoes)
   
    # Avaliação do desempenho de diferentes algoritmos para diferentes quantidades de números

# Variáveis globais necessárias:
medicoes = []                      # lista que armazena os resultados das medições em memória

# lista de algoritmos a testar (insira o seu, caso elabore outros):
algoritmos = {
    #'BSRT': { 'nome': 'Bubble sort', 'funcao': bubble_sort },
    'CSRT': { 'nome': 'Comb sort', 'funcao': comb_sort },
    'SSRT': { 'nome': 'Shake sort', 'funcao': shake_sort },
    #'QSTR': { 'nome': 'Quick sort tradicional', 'funcao': quick_sort}, # buga com numeros maiores que 100
    'QSMD': { 'nome': 'Quick sort melhorado', 'funcao': quick_sort2},    
    #  insira o seu aqui usando a sintaxe acima
}  

# testa o desempenho dos algoritmos para diferentes quantidades (múltiplos de 10):
for qtd in [10**x for x in range(1,5)]:
    max = qtd
    array = list(range(qtd, 0, -1))                   # array decrescente (pior caso)
   
    print('---------------------------------------------------')
    print('Testando algoritmos com array de tamanho ', qtd, 'decrescente.')
    print('---------------------------------------------------')
   
    print('Array gerado (', qtd, 'numeros ):\n' , array, '\n')
   
    for algoritmo in algoritmos:                       # itera sobre cada um dos algoritmos enunciados anteriormente
        print('=> Avaliando ordenação por "', algoritmos[algoritmo]['nome'], '"...')
       
        array_tmp = array.copy()                       # faz cópia do array para não perder
       
        tempo = time.process_time()                     # armazena o tempo de início do processamento
        m = algoritmos[algoritmo]['funcao'](array_tmp ) # aplica algorimo e retorna quantidade de trocas e comparações em 'm'
        t = time.process_time() - tempo                 # verifica o tempo de fim de processamento e calcula a diferença
        print('\nArray ordenado:\n', array_tmp, '\n', m)
       
        # armazena informações sobre a execução do algoritmo em um dicionário:
        medicao = {}
        medicao['algoritmo']=algoritmo
        medicao['tipo']='R'
        medicao['quantidade']=qtd
        medicao['trocas']=m['trocas']
        medicao['comparacoes']=m['comparacoes']
        medicao['tempo']=t
       
        medicoes.append(medicao)                              # adiciona medição em uma lista de medições

for qtd in [10**x for x in range(1,5)]:
    max = qtd
    array = list(range(0, qtd, +1))                   # array decrescente (pior caso)
   
    print('---------------------------------------------------')
    print('Testando algoritmos com array de tamanho ', qtd, ' crescente.')
    print('---------------------------------------------------')
   
    print('Array gerado (', qtd, 'numeros ):\n' , array, '\n')
   
    for algoritmo in algoritmos:                       # itera sobre cada um dos algoritmos enunciados anteriormente
        print('=> Avaliando ordenação por "', algoritmos[algoritmo]['nome'], '"...')
       
        array_tmp = array.copy()                       # faz cópia do array para não perder
       
        tempo = time.process_time()                     # armazena o tempo de início do processamento
        m = algoritmos[algoritmo]['funcao'](array_tmp ) # aplica algorimo e retorna quantidade de trocas e comparações em 'm'
        t = time.process_time() - tempo                 # verifica o tempo de fim de processamento e calcula a diferença
        print('\nArray ordenado:\n', array_tmp, '\n', m)
       
        # armazena informações sobre a execução do algoritmo em um dicionário:
        medicao = {}
        medicao['algoritmo']=algoritmo
        medicao['tipo']='R'
        medicao['quantidade']=qtd
        medicao['trocas']=m['trocas']
        medicao['comparacoes']=m['comparacoes']
        medicao['tempo']=t
       
        medicoes.append(medicao)                              # adiciona medição em uma lista de medições
for qtd in [10**x for x in range(1,5)]:
    max = qtd
    array = []
    for i in range (0, qtd):
        n = random.randint(0,qtd)
        array.append(n)
                      
   
    print('---------------------------------------------------')
    print('Testando algoritmos com array de tamanho ', qtd, ' com numeros aleatoriamente gerados')
    print('---------------------------------------------------')
   
    print('Array gerado (', qtd, 'numeros ):\n' , array, '\n')
   
    for algoritmo in algoritmos:                       # itera sobre cada um dos algoritmos enunciados anteriormente
        print('=> Avaliando ordenação por "', algoritmos[algoritmo]['nome'], '"...')
       
        array_tmp = array.copy()                       # faz cópia do array para não perder
       
        tempo = time.process_time()                     # armazena o tempo de início do processamento
        m = algoritmos[algoritmo]['funcao'](array_tmp ) # aplica algorimo e retorna quantidade de trocas e comparações em 'm'
        t = time.process_time() - tempo                 # verifica o tempo de fim de processamento e calcula a diferença
        print('\nArray ordenado:\n', array_tmp, '\n', m)
       
        # armazena informações sobre a execução do algoritmo em um dicionário:
        medicao = {}
        medicao['algoritmo']=algoritmo
        medicao['tipo']='R'
        medicao['quantidade']=qtd
        medicao['trocas']=m['trocas']
        medicao['comparacoes']=m['comparacoes']
        medicao['tempo']=t
       
        medicoes.append(medicao)                              # adiciona medição em uma lista de medições

print('Fim do processamento!')