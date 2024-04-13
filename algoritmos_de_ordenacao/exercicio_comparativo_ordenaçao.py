from quick_sort import quick_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort
import sys
import os
import random
import numpy as np
import timeit

diretorio_atual = os.path.dirname(__file__)
caminho_vetores = os.path.join(diretorio_atual, '..', 'Vetores')
sys.path.append(caminho_vetores)
from vetores_ordenados import VetorOrdenado

def insere_ordenado(valores):
    vetor = VetorOrdenado(len(valores))
    for i in valores:
        vetor.insere(i)
    return vetor
# Create a numpy array of random numbers
vetor = np.array([round(random.random(),4) for _ in range(5000)])
insere_ordenado(vetor.copy())


# Correct way to use timeit for each sorting algorithm
merge_sort_algorithm = timeit.Timer(lambda: merge_sort(vetor.copy())) 
quick_sort_algorithm = timeit.Timer(lambda: quick_sort(vetor.copy(), 0, len(vetor) - 1))  
bubble_sort_algorithm = timeit.Timer(lambda: bubble_sort(vetor.copy())) 
selection_sort_algorithm = timeit.Timer(lambda: selection_sort(vetor.copy()))
insertion_sort_algorithm = timeit.Timer(lambda: insertion_sort(vetor.copy()))
shell_sort_algorithm = timeit.Timer(lambda: shell_sort(vetor.copy()))

# Time each sorting algorithm
merge_sort_time = merge_sort_algorithm.timeit(number=1)
quick_sort_time = quick_sort_algorithm.timeit(number=1)
bubble_sort_time = bubble_sort_algorithm.timeit(number=1)
selection_sort_time = selection_sort_algorithm.timeit(number=1)
insertion_sort_time = insertion_sort_algorithm.timeit(number=1)
shell_sort_time = shell_sort_algorithm.timeit(number=1)

print("Sorted by Merge Sort:")
print(merge_sort(vetor.copy()))

print("Sorted by Quick Sort:")
print(quick_sort(vetor.copy(), 0, len(vetor) - 1))

print("Sorted by Bubble Sort:")
print(bubble_sort(vetor.copy()))

print("Sorted by Selection Sort:")
print(selection_sort(vetor.copy()))

print("Sorted by Insertion Sort:")
print(insertion_sort(vetor.copy()))

print("Sorted by Shell Sort:")
print(shell_sort(vetor.copy()))

# Print the times
print(f"Merge sort time: {round(merge_sort_time,4)} seconds")
print(f"Quick sort time: {round(quick_sort_time,4)} seconds")
print(f"Bubble sort time: {round(bubble_sort_time,4)} seconds")
print(f"Selection sort time: {round(selection_sort_time,4)} seconds")
print(f"Insertion sort time: {round(insertion_sort_time,4)} seconds")
print(f"Shell sort time: {round(shell_sort_time,4)} seconds")
