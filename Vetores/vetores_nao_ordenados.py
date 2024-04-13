import numpy as np

class VetorNaoOrdenado:
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
    
    # O(1) - O(2)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor está cheio")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
    
    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
        return -1
    
    #O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
                
vetor = VetorNaoOrdenado(5)
vetor.imprime() #vetor vazio sem elementos
vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
vetor.imprime()
# vetor.insere(7) #vetor cheio

pesquisa = vetor.pesquisar(5)

if pesquisa == -1:
    print("valor não encontrado")
else:
    print("valor encontrado na posição:", pesquisa)

exclui = vetor.excluir(8)
if exclui == -1:
    print("Valor não encontrado")
else:
    vetor.imprime()