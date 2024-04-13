import numpy as np

def shell_sort(vetor):
    intervalo = len(vetor) // 2
    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            valor = vetor[i]
            posicao = i
            while posicao >= intervalo and vetor[posicao - intervalo] > valor:
                vetor[posicao] = vetor[posicao - intervalo]
                posicao -= intervalo
            vetor[posicao] = valor
        intervalo = intervalo // 2
    return vetor

vetor = np.random.randint(0, 100, 10)

print(vetor)

vetor_ordenado = shell_sort(vetor)

print(vetor_ordenado)