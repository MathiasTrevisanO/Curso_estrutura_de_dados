import numpy as np
def selection_sort(vetor):
    n = len(vetor)
    
    for i in range(n):
        id_minimo = i
        for j in range(i + 1, n):
            if vetor[id_minimo] > vetor[j]:
                id_minimo = j
        temp = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp
            
    return vetor

vetor = np.random.randint(0, 100, 10)

print(vetor)

vetor_ordenado = selection_sort(vetor)

print(vetor_ordenado)