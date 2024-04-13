from vetor_ordenado_adjacentes import VetorOrdenadoAdjacentes

class BuscaAEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False
        
    def buscar(self, atual):
        print('--------------------------------')
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True
        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenadoAdjacentes(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()
            
            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)