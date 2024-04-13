from vetores_ordenados import VetorOrdenado
from vetores_nao_ordenados import VetorNaoOrdenado
import random
import timeit

elementos = []
for _ in range(10000):
    elementos.append(round(random.random(), 4))

def insere_nao_ordenado(lista):
    vetor = VetorNaoOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
    return vetor

def insere_ordenado(lista):
    vetor = VetorOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
    return vetor

def test_insere_nao_ordenado():
    insere_nao_ordenado(elementos)

def test_insere_ordenado():
    insere_ordenado(elementos)

# Time the execution
print("Tempo inserção utilizando não ordenado: ",timeit.timeit(test_insere_nao_ordenado, number=1))
print("Tempo inserção utilizando ordenado: ",timeit.timeit(test_insere_ordenado, number=1))

vetor_nao_ordenado = insere_nao_ordenado(elementos)
vetor_ordenado = insere_ordenado(elementos)

pesquisa = []

for _ in range(10000):
    pesquisa.append(round(random.random(), 4))

def pesquisa_nao_ordenada(lista):
    for i in lista:
        vetor_nao_ordenado.pesquisar(i)

def pesquisa_ordenada(lista):
    for i in lista:
        vetor_ordenado.pesquisa_binaria(i)

def test_pesquisa_ordenada():
    pesquisa_ordenada(pesquisa)

def test_pesquisa_nao_ordenada():
    pesquisa_nao_ordenada(pesquisa)
    
# Time the execution
print("Tempo pesquisa utilizando não ordenado: ",timeit.timeit(test_pesquisa_nao_ordenada, number=1))
print("Tempo pesquisa utilizando ordenado: ",timeit.timeit(test_pesquisa_ordenada, number=1))