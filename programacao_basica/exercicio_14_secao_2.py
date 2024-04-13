alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}
with open('alunos.txt', 'w') as file:
    for i in alunos:
        file.write(f'{i}, {alunos[i]}\n')

print(f'Arquivos alunos.txt salvo com sucesso')

with open('alunos.txt', 'r') as file:
    for i in alunos:
        print(i)