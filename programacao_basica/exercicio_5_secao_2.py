def media_notas(notas):
    soma = 0 
    for nota in notas:
        soma += nota  
    return soma / len(notas)

def main():
    notas = []
    for i in range(0, 5):
        nota = float(input(f"Digite a nota {i+1}:"))
        notas.append(nota)
    media = media_notas(notas)
    print("A média das notas foi: {}".format(media))


if __name__ == '__main__':
    main()
