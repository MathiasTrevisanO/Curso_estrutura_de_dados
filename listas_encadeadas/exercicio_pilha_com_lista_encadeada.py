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
        novo.proximo = self.primeiro  # type: ignore
        self.primeiro = novo

    def verifica_lista_vazia(self):
        if self.primeiro == None:  # type: ignore
            print("Lista está vazia...")
            return None

    def excluir_inicio(self):
        self.verifica_lista_vazia()
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo  # type: ignore
        return temp


class PilhaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeada()

    def empilhar(self, valor):
        self.lista.insere_inicio(valor)

    def desempilhar(self):
        return self.lista.excluir_inicio()

    def verifica_pilha_vazia(self):
        if self.lista.primeiro == None:  # type: ignore
            print("Pilha está vazia...")

    def ver_topo(self):

        if self.lista.primeiro is not None:
            return self.lista.primeiro.valor
        else:
            return self.verifica_pilha_vazia()
            


pilha = PilhaListaEncadeada()

print("Empilhando o 5 e o 3...")
pilha.empilhar(5)
pilha.empilhar(3)

print("Topo da pilha: ",pilha.ver_topo())

print("Desempilhando o topo...")
pilha.desempilhar()
print("Topo da pilha: ",pilha.ver_topo())

print("Desempilhando o elemento 5 para ficar vazia...")
pilha.desempilhar()
print("Topo da pilha: ",pilha.ver_topo())