from pilha_em_grafos import Pilha
from busca_em_profundidade import BuscaProfundidade
from busca_em_largura import BuscaLargura
from fila_em_grafos import FilaCircular
from vetor_ordenado_distancia_objetivo import VetorOrdenadoDisObjetivo
from busca_gulosa import BuscaGulosa
from vetor_ordenado_adjacentes import VetorOrdenadoAdjacentes
from busca_aestrela import BuscaAEstrela

class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []
    
    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
    
    def mostra_adjacentes(self):
        for adjacente in self.adjacentes:
            print(adjacente.vertice.rotulo, adjacente.custo)
    
class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo
    
class Grafo:
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)
    
    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))
    
    zerind.adiciona_adjacente(Adjacente(arad,75))
    zerind.adiciona_adjacente(Adjacente(oradea,71))
    
    oradea.adiciona_adjacente(Adjacente(zerind,71))
    oradea.adiciona_adjacente(Adjacente(sibiu,151))
    
    sibiu.adiciona_adjacente(Adjacente(arad,140))
    sibiu.adiciona_adjacente(Adjacente(oradea,151))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))
    sibiu.adiciona_adjacente(Adjacente(fagaras,99))
    
    timisoara.adiciona_adjacente(Adjacente(arad,118))
    timisoara.adiciona_adjacente(Adjacente(lugoj,111))
    
    lugoj.adiciona_adjacente(Adjacente(timisoara,111))
    lugoj.adiciona_adjacente(Adjacente(mehadia,75))
    
    mehadia.adiciona_adjacente(Adjacente(lugoj,70))
    mehadia.adiciona_adjacente(Adjacente(dobreta,75))

    dobreta.adiciona_adjacente(Adjacente(mehadia,75))
    dobreta.adiciona_adjacente(Adjacente(craiova,120))
    
    craiova.adiciona_adjacente(Adjacente(dobreta,120))
    craiova.adiciona_adjacente(Adjacente(rimnicu,146))
    craiova.adiciona_adjacente(Adjacente(pitesti,138))
    
    rimnicu.adiciona_adjacente(Adjacente(craiova,146))
    rimnicu.adiciona_adjacente(Adjacente(pitesti,97))
    rimnicu.adiciona_adjacente(Adjacente(sibiu,80))
    
    pitesti.adiciona_adjacente(Adjacente(rimnicu,97))
    pitesti.adiciona_adjacente(Adjacente(craiova,138))
    pitesti.adiciona_adjacente(Adjacente(bucharest,101))
    
    bucharest.adiciona_adjacente(Adjacente(pitesti,101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu,90))
    bucharest.adiciona_adjacente(Adjacente(fagaras,211))
    
    giurgiu.adiciona_adjacente(Adjacente(bucharest,90))
    
    fagaras.adiciona_adjacente(Adjacente(sibiu,99))
    fagaras.adiciona_adjacente(Adjacente(bucharest,211))
    

grafo = Grafo()
print("Adjacentes...\n")
grafo.arad.mostra_adjacentes()

print('------------------------------------------------\n')
print('Busca em profundidade:\n')
busca_profundidade = BuscaProfundidade(grafo.arad)
# busca_profundidade.buscar()

print('------------------------------------------------\n')
print('Busca em largura:\n')
busca_largura = BuscaLargura(grafo.arad)
# busca_largura.buscar()
# print('\nNúmero de elementos na fila: ', busca_largura.fila.numero_elementos)

print('------------------------------------------------\n')
print('Busca gulosa:\n')
# busca_gulosa = BuscaGulosa(grafo.bucharest)
# busca_gulosa.buscar(grafo.arad)

print('------------------------------------------------\n')
print('Busca A Estrela (A*):\n')
busca_aestrela = BuscaAEstrela(grafo.bucharest)
busca_aestrela.buscar(grafo.arad)