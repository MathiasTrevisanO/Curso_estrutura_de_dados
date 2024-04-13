def calculo_media(n1, n2, n3):
    return (n1+n2+n3) / 3
def main():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    media = calculo_media(n1, n2, n3)
    if media >= 0 and media <= 4:
        print("Aluno reprovado")
    elif media >= 4.1 and media <= 6:
        print("Aluno em exame.")
        n4 = float(input("Nota do exame: "))
        if n4 > 6:
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")
    elif media > 6:
        print("Aluno aprovado")

if __name__ == "__main__":
    main()
        