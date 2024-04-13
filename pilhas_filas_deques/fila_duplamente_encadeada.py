class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None # type: ignore

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo # type: ignore
            novo.proximo = self.primeiro # type: ignore
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            novo.anterior = self.ultimo # type: ignore
            self.ultimo.proximo = novo # type: ignore
        self.ultimo = novo

    def excluir_inicio(self):
        temp = self.primeiro
        if self.__lista_vazia(): # type: ignore
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo # type: ignore
            self.primeiro.anterior = None # type: ignore
        return temp

    def excluir_final(self):
        temp = self.ultimo
        if self.__lista_vazia(): # type: ignore
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None # type: ignore
            self.ultimo = self.ultimo.anterior # type: ignore
        return temp
    
    def excluir_posicao(self, valor):
        atual = self.primeiro
        while atual.valor != valor: # type: ignore
            atual = atual.proximo # type: ignore
            if atual == None:
                return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo # type: ignore
        else:
            atual.anterior.proximo = atual.proximo # type: ignore
        if atual == self.ultimo: 
            self.ultimo = atual.anterior # type: ignore
        else:
            atual.proximo.anterior = atual.anterior # type: ignore
        return atual

    def mostrar_frente(self):
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_tras(self):
        atual = self.ultimo
        while atual is not None:
            atual.mostra_no()
            atual = atual.anterior


lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
print("mostrar frente...")
lista.mostrar_frente()
print(lista.primeiro, lista.ultimo)
print(lista.primeiro.valor, lista.ultimo.valor) # type: ignore

print("mostrar tras...")
lista.mostrar_tras()

lista.insere_final(6)
lista.insere_final(7)
print("mostrar frente com o elemento 6 e 7 adicionado na lista...")
lista.mostrar_frente()

lista.excluir_final()
lista.excluir_inicio()
print("Excluindo o elemento do inicio e do final...")
lista.mostrar_frente()

print("excluindo o elemento 2:")
lista.excluir_posicao(2)
lista.mostrar_frente()
