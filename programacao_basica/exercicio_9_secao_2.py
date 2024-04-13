import numpy as np

matriz = np.array([[3, 4, 1],
                    [3, 1, 5]])

soma = 0

for linha in matriz:
    soma = soma + linha.sum()
    

print(soma)
    