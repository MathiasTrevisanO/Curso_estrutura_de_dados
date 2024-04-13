def read_string(mensagem):
    return mensagem

def read_float(num_float):
    return num_float

def main():
    mensagem = read_string(input("Digite uma mensagem: "))
    num_float = read_float(input("Digite um valor tipo float:"))
    
    print(mensagem)
    print(num_float)

if __name__ == "__main__":
    main()