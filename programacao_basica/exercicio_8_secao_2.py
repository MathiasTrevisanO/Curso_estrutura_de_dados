
def media(dict):
    soma = 0
    for i in dict:
        soma += dict[i]
    media = soma / len(dict)
    print(f"A média é igual a {media:.1f}")


def main():
    dict = {}
    for i in range(0, 3):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        nota = float(input(f"Nota do aluno {nome}: "))
        dict[nome] = nota
        
    media(dict)

if __name__ == "__main__":
    main()
    