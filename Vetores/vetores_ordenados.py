import numpy as np 

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=float)
    
    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print("Vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])
    
    #O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor está cheio")
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
                
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = valor
        self.ultima_posicao += 1
    
    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
            if self.valores[i] > valor or i == self.ultima_posicao:
                return -1
    
    # O(log n)
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        while True:
            meio = int((limite_inferior + limite_superior) / 2)
            #Se achou na primeira tentativa
            if self.valores[meio] == valor:
                return meio
             #Se não achou
            if limite_inferior > limite_superior:
                return -1
            if self.valores[meio] > valor:
                limite_superior = meio - 1
            else:
                limite_inferior = meio + 1
           

    #O(n)
    def excluir(self, valor):
        posicao = self.pesquisa_linear(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao): # type: ignore
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
            
vetor = VetorOrdenado(10)
vetor.imprime()

vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(1)
vetor.insere(8)
vetor.imprime()


#PESQUISA LINEAR
pesquisa = vetor.pesquisa_linear(8)

if pesquisa == -1:
    print("Valor não encontrado")
else:
    print("Valor encontrado na posição:", pesquisa)
    
exclui = vetor.excluir(8)
if exclui == -1:
    print("Valor não encontrado")
else:
    vetor.imprime()
    
#PESQUISA BINÁRIA

pesquisa_binaria = vetor.pesquisa_binaria(6)

if pesquisa_binaria == -1:
    print("Valor não encontrado")
else:
    print("Valor encontrado na posição:", pesquisa_binaria)