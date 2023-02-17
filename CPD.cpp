// Atenção: usa código C++11
// para saber se o seu compilador tem suporte, execute: 
// cout << __cplusplus;
// O resultado deve ser 201103L ou maior.
// o do google collab é C++14 
// A grande maioria dos compiladores atuais suporta nativamente c++11. 
// Outros exigem a configuração de parâmetros de compilação... Verifique a documentação do seu.

#include<iostream>
#include<tuple>
#include<random>
#include<bits/stdc++.h>

//TODO: executar várias vezes os algoritmos, com tamanhos diferentes (e.g., 100, 1000 e 10000)

#define MAX 10000                                                               // quantidade de números no array

using namespace std;

typedef int array_size_t;                                                       // Tipo para especificar tamanho do array
typedef int* array_t;                                                           // Tipo para especificar formato do array
typedef std::tuple<int, int> loginfo_t;                                         // armazena contagem de comparações e trocas  
typedef std::mt19937 MyRNG;                                                     // Gerador de números aleatórios do tipo Mersenne Twister Random Generator 

MyRNG rng;                                                                      // gerador de números aleatórios
uint32_t seed_val;                                                              // semente de geração de números

loginfo_t insertion_sort(array_t, array_size_t);
loginfo_t insertion_sortBB(array_t, array_size_t);
loginfo_t shellsort(array_t, array_size_t);
std::tuple<int, int, int> busca_binaria(array_t, int, int, int);                // retorna uma tupla contendo <posicao, qtd de trocas, qtd de comparações>

int main(void){    
    // cout << __cplusplus << endl;                                             // verifica versão do compilador
    rng.seed(seed_val);                                                         // inicializa semente de geração de números aleatórios    
    
    loginfo_t loginfo;                                                          // armazena contadores de comparações e trocas (ver typedef acima)

    int* array = new int[MAX];
    int* salva = new int[MAX];
    int tam = MAX;
    uniform_int_distribution<> distrib(0, MAX);                             // cria gerador com distribuição uniforme entre 0 e MAX_INT                                                 // array dinâmico que armazena os números

   
    
    do
    {   
        cout<< "---------------------Array's de tamanho "<< tam << "---------------------"<< endl;
        //DECRESS///////////////////////////////////////////////////////
        for(auto i=0;i<tam;i++) array[i] = tam-i; // gera números em ordem decrescente
        cout << endl;
        cout << endl <<"-----------------DECRESCENTE Array gerado: ";
        for(auto i=0;i<tam;i++) cout << array[i] << " ";
        cout << endl;
        
        // TODO: testar os outros algoritmos (insertion_sortBB e shellsort)
        cout << endl<<"-------------------------------------------Insertion Sort DECRESCENTE "<< tam << "-------------------------------------------------" << endl;
        loginfo = insertion_sort(array, tam);
        cout << endl << "Array ordenado: ";
        for(auto i=0;i<tam;i++) cout << array[i] << " ";                               
        cout <<endl <<"Quantidade de trocas: " << get<0>(loginfo) << endl;
        cout << "Quantidade de comparações: " << get<1>(loginfo) << endl;

        for(auto i=0;i<tam;i++) array[i] = tam-i;

        cout<< endl <<"-------------------------------------------Insertion Sort Binary DECRESCENTE "<< tam<< "-------------------------------------------------";
        loginfo = insertion_sortBB(array,tam);
        cout << endl << "Array ordenado: ";                               
        for(auto i=0;i<tam;i++) cout << array[i] << " ";
        cout << endl <<"Quantidade de trocas: " << get<0>(loginfo) << endl;
        cout << "Quantidade de comparações: " << get<1>(loginfo) << endl;

        for(auto i=0;i<tam;i++) array[i] = tam-i;

        cout << endl<<"-------------------------------------------Shell Sort DECRESCENTE "<< tam<< "-------------------------------------------------" << endl;
        loginfo = shellsort(array,tam);
        

        cout << endl;
        cout << endl <<"Quantidade de trocas: " << get<0>(loginfo) << endl;
        cout << "Quantidade de comparações: " << get<1>(loginfo) << endl;
        cout << endl << "Array ordenado: ";                               
        for(auto i=0;i<tam;i++) cout << array[i] << " ";
        




        //CRESCENT//////////////////////////////////////////////////////
        for(auto i=0;i<tam;i++) array[i] = i;
        cout << endl;     // gera números em ordem crescente
        cout << endl << "-----------------CRESCENTE Array gerado: ";
        for(auto i=0;i<tam;i++) cout << array[i] << " ";
        cout << endl;

        // TODO: testar os outros algoritmos (insertion_sortBB e shellsort)
        cout << endl<<"-------------------------------------------Insertion Sort CRESCENTE "<< tam <<  "-------------------------------------------------" << endl;
        loginfo = insertion_sort(array, tam);
        cout << endl << "Array ordenado: ";
        for(auto i=0;i<tam;i++) cout << array[i] << " ";                               
        cout <<endl <<"Quantidade de trocas: " << get<0>(loginfo) << endl;
        cout << "Quantidade de comparações: " << get<1>(loginfo) << endl;

        for(auto i=0;i<tam;i++) array[i] = i;

        cout<< endl <<"-------------------------------------------Insertion Sort Binary CRESCENTE "<< tam <<"-------------------------------------------------";
        loginfo = insertion_sortBB(array,tam);
        cout << endl << "Array ordenado: ";                               
        for(auto i=0;i<tam;i++) cout << array[i] << " ";
        cout << endl <<"Quantidade de trocas: " << get<0>(loginfo) << endl;
        cout << "Quantidade de comparações: " << get<1>(loginfo) << endl;

        for(auto i=0;i<tam;i++) array[i] = i;

        cout << endl<<"-------------------------------------------Shell Sort CRESCENTE "<< tam<< "-------------------------------------------------" << endl;
        loginfo = shellsort(array,tam);
        

        cout << endl;
        cout << endl <<"Quantidade de trocas: " << get<0>(loginfo) << endl;
        cout << "Quantidade de comparações: " << get<1>(loginfo) << endl;
        cout << endl << "Array ordenado: ";                               
        for(auto i=0;i<tam;i++) cout << array[i] << " ";


        //RNG////////////////////////////////////////////////////////
        for(auto i=0;i<tam;i++) array[i] = distrib(rng); // aleatoriamente
        for(auto i = 0; i < tam; i++) salva[i] = array[i];
        cout << endl;
        cout << endl <<"-----------------ALEATORIO Array gerado:";
        for(auto i=0;i<tam;i++) cout << array[i] << " ";
        cout << endl;

        // TODO: testar os outros algoritmos (insertion_sortBB e shellsort)
        cout << endl<<"-------------------------------------------Insertion Sort ALEATORIO "<<tam<<"------------------------------------------------- " << endl;
        loginfo = insertion_sort(array, tam);
        cout << endl << "Array ordenado: ";
        for(auto i=0;i<tam;i++) cout << array[i] << " ";                               
        cout <<endl <<"Quantidade de trocas: " << get<0>(loginfo) << endl;
        cout << "Quantidade de comparações: " << get<1>(loginfo) << endl;

        for(auto i=0;i<tam;i++) array[i] = salva[i]; // aleatoriamente

        cout<< endl <<"-------------------------------------------Insertion sort Binary ALEATORIO "<< tam<< "-------------------------------------------------";
        loginfo = insertion_sortBB(array,tam);
        cout << endl << "Array ordenado: ";                               
        for(auto i=0;i<tam;i++) cout << array[i] << " ";
        cout << endl <<"Quantidade de trocas: " << get<0>(loginfo) << endl;
        cout << "Quantidade de comparações: " << get<1>(loginfo) << endl;
        
        for(auto i=0;i<tam;i++) array[i] = salva[i]; // aleatoriamente

        cout << endl<<"-------------------------------------------Shell Sort ALEATORIO "<< tam<<"-------------------------------------------------" << endl;
        loginfo = shellsort(array,tam);
        

        cout << endl;
        cout << endl <<"Quantidade de trocas: " << get<0>(loginfo) << endl;
        cout << "Quantidade de comparações: " << get<1>(loginfo) << endl;
        cout << endl << "Array ordenado: ";                               
        for(auto i=0;i<tam;i++) cout << array[i] << " ";
        cout << endl;

        

        tam  = tam / 10; 
    } while ((tam / 1) != 1);
    
    
    

    // TODO: mostrar informações de execução de todos os algoritmos

    delete[] array;
    return 0;
}

// Função de Inserção Direta com Busca Linear
loginfo_t insertion_sort(array_t array, array_size_t array_size){
    int trocas = 0, comparacoes = 0;
    for(int i=1;i<array_size;i++){                                              // do segundo ao último
        auto chave = array[i];                                                  // chave a inserir no subarray ordenado
        auto j = i-1;                                                           // último elemento do subarray ordenado         
        comparacoes = comparacoes + 1;
        while(j >= 0 && array[j] > chave){                                      // busca linear da direita para a esquerda no subarray ordenado   
            comparacoes = comparacoes + 1;
            array[j+1] = array[j];
            j = j - 1;
            trocas = trocas + 1;
        }
        if(j+1 != i){ 
           array[j+1] = chave;
           trocas = trocas + 1;
       }
    }
    return make_tuple(trocas, comparacoes);                                     // retorna quantidade de operações
}

loginfo_t insertion_sortBB(array_t array, array_size_t array_size){    
   int trocas = 0, comparacoes = 0;
   std::tuple<int, int, int> info;
   int i, local, j, elemento;
   for(i = 1; i < array_size; ++i) {
      j = i - 1;
      elemento = array[i];
      info = busca_binaria(array, elemento, 0, j);
      local = get<0>(info);
      trocas += get<1>(info);
      comparacoes += get<2>(info)+1;
      while (j >= local) {
         trocas++;
         array[j+1] = array[j];
         j--;
      }
      if(j+1 != i){ 
           array[j+1] = elemento;
           trocas = trocas + 1;
       }
   }
    return make_tuple(trocas, comparacoes);                                     // retorna quantidade de operações
}

// *****************************************************
//  TODO: Implementação dos seus algoritmos (a seguir)

// Faz busca binária do 'elemento' no 'array', entre os índices 'inicio' e 'fim'
// retorna posição do elemento, quantidade de trocas e quantidade de comparações
std::tuple<int, int, int> busca_binaria(array_t array, int elemento, int inicio, int fim){
   int comparacoes = 0, trocas = 0;

   while (inicio <= fim){

    
        int meio = (inicio + fim) / 2;
    
        if (elemento == array[meio])
            return make_tuple(meio + 1, trocas, comparacoes);
    
        if (elemento > array[meio])
        {
            inicio = meio +1;
            comparacoes ++;
        }
            
        if(elemento < array[meio])
        {
            fim = meio -1;
            comparacoes++;
        }
            
   }
    return make_tuple(inicio, trocas,comparacoes);
}

loginfo_t shellsort(array_t array, array_size_t array_size){
    int trocas = 0, comparacoes = 0;

    
    for (int espaco = array_size/2; espaco > 0; espaco /= 2)
    {
        
        comparacoes ++;
        for (int i = espaco; i < array_size; i += 1)
        {
           
            int var = array[i];
            trocas++;
           
            int j;           
            for (j = i; j >= espaco && array[j - espaco] > var; j -= espaco)
            {
                array[j] = array[j - espaco];
                
                comparacoes ++;
            }
                
             trocas++;
            array[j] = var;
        }
    }
    
    // defina aqui sua versão da função shellsort    
    
    return make_tuple(trocas, comparacoes);                                     // retorna quantidade de operações
}