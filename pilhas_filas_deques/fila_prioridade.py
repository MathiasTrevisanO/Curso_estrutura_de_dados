import numpy as np

class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)
    
    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def __fila_vazia(self):
        return self.numero_elementos == 0
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("Fila está cheia")
            return
        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos - 1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x + 1] = valor
            self.numero_elementos += 1
    
    def defileirar(self):
        if self.__fila_vazia():
            print("Fila está vazia")
            return -1
        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor
    
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        else:
            return self.valores[self.numero_elementos - 1]
        
fila = FilaPrioridade(5)
# print(fila.primeiro())

fila.enfileirar(30)
fila.enfileirar(50)
fila.enfileirar(10) #fila de prioridade o valor 10 fica em primeiro na fila
print(fila.primeiro())
fila.enfileirar(40)
fila.enfileirar(20)
print(fila.valores)
fila.enfileirar(100)