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
    
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__verifica_lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro # type: ignore
        self.primeiro = novo
    
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
        
    def mostrar(self):
        if self.__verifica_lista_vazia():
            print("A lista está vazia")
            return
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

lista = ListaEncadeadaExtremidadeDupla()
print("Elementos inseridos no início da lista:")
lista.insere_inicio(1)
print(lista.primeiro, lista.ultimo)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()
print(lista.primeiro, lista.ultimo)

print("Elementos inseridos no final da lista:")
lista.insere_final(6)
lista.mostrar()

print("Excluir elemento no inicio da lista:")
lista.excluir_inicio()
lista.mostrar()