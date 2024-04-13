import numpy as np 

class VetorOrdenadoAdjacentes:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)
    
    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print("Vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.rotulo, ' - ', 
                      self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objetivo, ' - ',
                      self.valores[i].distancia_aestrela)
    
    #O(n)
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor está cheio")
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
                
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1
    
            
