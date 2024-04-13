
def ler_temperatura():
    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    return temperatura

def conversao(temperatura):
    return (9 * temperatura + 160) / 5

def mostrar_valor(valor_convertido):
    print("Valor em Fahrenheit:", valor_convertido)

def main():
    temperatura = ler_temperatura()
    conversao_fahrenheit = conversao(temperatura)
    mostrar_valor(conversao_fahrenheit)

if __name__ == "__main__":
    main()    