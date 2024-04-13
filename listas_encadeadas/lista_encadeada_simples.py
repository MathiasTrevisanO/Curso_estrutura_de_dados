import numpy as np 

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
    def mostra_no(self):
        print(self.valor)
    
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
    
    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro # type: ignore
        self.primeiro = novo
    
    def verifica_lista_vazia(self):
        if self.primeiro == None: # type: ignore
            print("Lista está vazia...")
            return None
    
    def mostrar(self):
        self.verifica_lista_vazia()
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo
    
    def excluir_inicio(self):
        self.verifica_lista_vazia()
        temp = self.primeiro      
        self.primeiro = self.primeiro.proximo # type: ignore
        return temp
    
    def excluir_posicao(self,valor):
        self.verifica_lista_vazia()
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor: # type: ignore
            if atual.proximo == None: # type: ignore
                return None
            else:
                anterior = atual
                atual = atual.proximo # type: ignore
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo # type: ignore
        else:
            anterior.proximo = atual.proximo # type: ignore
        return atual
    
    
    def pesquisa(self, valor):
        self.verifica_lista_vazia()
        atual = self.primeiro
        while atual.valor != valor: # type: ignore
            if atual.proximo == None: # type: ignore
                return None
            else:
                atual = atual.proximo # type: ignore
        return atual

no1 = No(1)
no1.mostra_no()

no2 = No(2)
no2.mostra_no()
print("\nLISTA ENCADEADA INSERÇÃO do INICIO \n")
lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
print(lista.primeiro)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()


print("\nLISTA ENCADEADA EXCLUSÃO DO INICIO \n")
lista.excluir_inicio()
lista.excluir_inicio()
lista.mostrar()
print(lista.primeiro)

pesquisa = lista.pesquisa(3)
if pesquisa != None:
    print("Valor encontrado: ", pesquisa.valor)
else:
    print("Valor não encontrado")
    
print("\nLISTA ENCADEADA EXCLUSÃO DE UMA POSIÇÃO \n")
lista.excluir_posicao(2)
lista.mostrar()