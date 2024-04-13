from pilha_em_grafos import Pilha

class BuscaProfundidade:
    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.pilha = Pilha(20)
        self.pilha.empilhar(inicio)
    
    def buscar(self):
        topo = self.pilha.ver_topo()
        print('\nTopo: {}'.format(topo.rotulo)) # type: ignore
        for adjacente in topo.adjacentes: # type: ignore
            print('Topo é {}. {} já foi visitada? {}'.format(topo.rotulo, adjacente.vertice.rotulo, adjacente.vertice.visitado)) # type: ignore
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.pilha.empilhar(adjacente.vertice)
                print('Empilhou {}\n'.format(adjacente.vertice.rotulo))
                self.buscar()
        print('Desempilhou: {}'.format(self.pilha.desempilhar().rotulo)) # type: ignore
