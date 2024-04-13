class Idade:
    def __init__(self, idade):
        self.idade = idade
    
    def crianca(self):
        if self.idade >= 0 and self.idade <= 12:
            print("O usuário é uma criança")
    
    def adolescente(self):
        if self.idade > 12 and self.idade <= 18:
            print("O usuário é um adolescente")
    
    def adulto(self):
        if self.idade > 18:
            print("O usuário é um adulto")
    
    def idade_invalida(self):
        if self.idade < 0:
            print("Idade inválida")
    
def main():
    idade = int(input("Digite sua idade: "))
    idade_obj = Idade(idade)
    idade_obj.crianca()
    idade_obj.adolescente()
    idade_obj.adulto()
    idade_obj.idade_invalida()
if __name__ == "__main__":
    main()