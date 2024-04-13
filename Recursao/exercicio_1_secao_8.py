
def fatorial(m):
    if m == 1 or m == 0:
        return 1
    else:
        return m*fatorial(m - 1)
    

num = int(input("Digite um numero fatorial não negativo:"))
if num < 0:
    print("Valor negativo...")
else:
    print(fatorial(num))