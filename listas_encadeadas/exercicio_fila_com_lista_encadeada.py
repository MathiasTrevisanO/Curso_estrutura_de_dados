import numpy as np 

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
    def mostra_no(self):
        print(self.valor)
        
class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def __verifica_lista_vazia(self):
        return self.primeiro == None
    
    def insere_final(self, valor):
        novo = No(valor)
        if self.__verifica_lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo # type: ignore
        self.ultimo = novo
        
    def excluir_inicio(self):
        if self.__verifica_lista_vazia():
            print("A lista está vazia")
            return
        temp = self.primeiro
        if self.primeiro.proximo == None: # type: ignore
            self.ultimo = None
        self.primeiro = self.primeiro.proximo # type: ignore
        return temp

            
class FilaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeadaExtremidadeDupla()
    
    def enfileirar(self, valor):
        self.lista.insere_final(valor)
        
    
    def desenfileirar(self):
        self.lista.excluir_inicio()
    
    def fila_vazia(self):
        return self.lista.__verifica_lista_vazia()
    
    def ver_inicio(self):
        if self.lista.primeiro == None:
            return None
        else:
            return self.lista.primeiro.valor
    
fila = FilaListaEncadeada()
print("Enfileirando 1,2,3,4,5...")
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
print("Verificando a primeira pessoa na fila:", fila.ver_inicio())

print("Primeira pessoa atendida...")
fila.desenfileirar()
print("Proxima pessoa a ser atendida: ", fila.ver_inicio())

print("Atendendo todos da fila...")
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
print("Status da fila: ")
if fila.ver_inicio() == None:
    print("A fila está vazia")
else:
    print("A fila não está vazia")