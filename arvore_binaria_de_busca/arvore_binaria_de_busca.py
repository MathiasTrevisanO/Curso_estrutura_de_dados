import os
import graphviz

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
    def mostra_no(self):
        print(self.valor)

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual                
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo # type: ignore
                        return
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo # type: ignore
                        return
    
    def pesquisar(self, valor):
        atual = self.raiz
        while atual.valor != valor: # type: ignore
            if valor < atual.valor: # type: ignore
                atual = atual.esquerda # type: ignore
            else:
                atual = atual.direita # type: ignore
            if atual == None:
                return None
        return atual
    
    def get_sucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita
        while atual != None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
        return sucessor  
    
    def excluir(self, valor):
        if self.raiz == None:
            print("A arvore está vazia")
            return False
        atual = self.raiz
        pai = self.raiz
        e_esquerda = True
        while atual.valor != valor:
            pai = atual
            if valor < atual.valor:
                atual = atual.esquerda
                e_esquerda = True
            else:
                atual = atual.direita
                e_esquerda = False
            if atual == None:
                return False
        #Validação se o nó é uma folha
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda == True:
                pai.esquerda = None
            else:
                pai.direita = None
        #Validação se o nó tem somente um filho
        elif atual.direita == None:
            if atual == self.raiz:
                self.raiz = atual.esquerda
            elif e_esquerda == True:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda
        elif atual.esquerda == None:
            if atual == self.raiz:
                self.raiz = atual.direita
            elif e_esquerda == True:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita
        #Validação se o nó tem dois filhos
        else:
            sucessor = self.get_sucessor(atual)   
            if atual == self.raiz:
                self.raiz = sucessor
            elif e_esquerda == True:
                pai.esquerda = sucessor # type: ignore
            else:
                pai.direita = sucessor # type: ignore
                
            sucessor.esquerda = atual.esquerda
            
        return True
    
    def pre_ordem(self, no):
        if no != None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)
            
    def ordem(self, no):
        if no != None:
            self.ordem(no.esquerda)
            print(no.valor)
            self.ordem(no.direita)
    
    def pos_ordem(self, no):
        if no != None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)
                    
    def get_graph(self):
        dot = graphviz.Digraph()
        self._adicionar_nos(self.raiz, dot)
        return dot
    
    def _adicionar_nos(self, no, dot):
        if no is not None:
            if no.esquerda is not None:
                dot.edge(str(no.valor), str(no.esquerda.valor))
            if no.direita is not None:
                dot.edge(str(no.valor), str(no.direita.valor))
            self._adicionar_nos(no.esquerda, dot)
            self._adicionar_nos(no.direita, dot)
    
    def _verifica_se_encontrou(self, key):
        if key == False:
            print("Valor não encontrado")
        else:
            print("Valor excluído com sucesso")
            

arvore = ArvoreBinariaBusca()

#Inserção
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)
arvore.inserir(89)          

#Pesquisa
no = 61
if arvore.pesquisar(no) == None:
    print("Valor não encontrado")
else:
    print(f"Valor {arvore.pesquisar(no).valor} encontrado") # type: ignore

#Travessia
print("\nTravessia em pre ordem:")
arvore.pre_ordem(arvore.raiz)

print("\nTravessia em ordem:")
arvore.ordem(arvore.raiz)

print("\nTravessia em pós ordem:")
arvore.pos_ordem(arvore.raiz)

# Gera a imagem da árvore
tree_graph = arvore.get_graph()
script_dir = os.path.dirname(__file__)
image_dir = os.path.join(script_dir, "figures")
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

image_1 = os.path.join(image_dir, "binary_search_tree.png")
tree_graph.render(image_1, format="png", cleanup=True)

# Exclusão de um nó folha
key_delete1 = arvore.excluir(9)
arvore._verifica_se_encontrou(key_delete1)

tree_graph = arvore.get_graph()
image_2 = os.path.join(image_dir, "node_9_removed.png")
tree_graph.render(image_2, format="png", cleanup=True)

# Exclusão de um nó raiz que tem somente um filho
key_delete2 = arvore.excluir(14)
arvore._verifica_se_encontrou(key_delete2)

tree_graph = arvore.get_graph()
image_3 = os.path.join(image_dir, "node_14_removed.png")
tree_graph.render(image_3, format="png", cleanup=True)

# Verifica o sucessor da raiz
print(f"O Sucessor do nó {arvore.raiz.valor} é:",arvore.get_sucessor(arvore.raiz).valor) # type: ignore

# Exclusão de um nó raiz que tem dois filhos
key_delete3 = arvore.excluir(30)
arvore._verifica_se_encontrou(key_delete3)

tree_graph = arvore.get_graph()
image_4 = os.path.join(image_dir, "node_30_removed.png")
tree_graph.render(image_4, format="png", cleanup=True)
