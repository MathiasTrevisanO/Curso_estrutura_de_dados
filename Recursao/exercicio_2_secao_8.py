def potencia(a,b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b - 1)


a = int(input("Digite um numero da base da potencia(não negativo):"))
b = int(input("Digite um numero do expoente da potencia(não negativo):"))
if a < 0 or b < 0:
    print("Valor negativo...")
else:
    print(potencia(a,b))