from fila_em_grafos import FilaCircular
class BuscaLargura:
    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.fila = FilaCircular(20)
        self.fila.enfileirar(inicio)
        
    def buscar(self):
        primeiro = self.fila.primeiro()
        print('\nPrimeiro da fila: {}'.format(primeiro.rotulo)) # type: ignore
        temp = self.fila.desenfileirar()
        print('Desenfileirou: {}'.format(temp.rotulo)) # type: ignore
        for adjacente in primeiro.adjacentes: # type: ignore
            print('Primeiro elemento era {}. {} já foi visitado? {}'.format(temp.rotulo, adjacente.vertice.rotulo, adjacente.vertice.visitado)) # type: ignore
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.fila.enfileirar(adjacente.vertice)
                print('Enfileirou: {}'.format(adjacente.vertice.rotulo))
        if self.fila.numero_elementos > 0:
            self.buscar()
                