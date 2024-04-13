import numpy as np

def insertion_sort(vetor):
    n = len(vetor)
    for i in range(1, n):
        marcado = vetor[i]
        j = i - 1
        while j >= 0 and marcado < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = marcado
    
    return vetor
        
    

vetor = np.random.randint(0, 100, 10)

print(vetor)

vetor_ordenado = insertion_sort(vetor)

print(vetor_ordenado)