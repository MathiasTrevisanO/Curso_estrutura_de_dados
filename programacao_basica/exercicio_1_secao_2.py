class Operacoes:
    
    def adicao(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        return a / b
    
def main():
    operacao = Operacoes()
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    
    res_soma = operacao.adicao(a, b)
    print(f"O resultado de {a}+{b}={res_soma}.")
    res_subtracao = operacao.subtracao(a, b)
    print(f"O resultado de {a}-{b}={res_subtracao}.")
    res_multiplicacao = operacao.multiplicacao(a, b)
    print(f"O resultado de {a}*{b}={res_multiplicacao}.")
    res_divisao = operacao.divisao(a, b)
    print(f"O resultado de {a}/{b}={res_divisao}.")
    
if __name__ == '__main__':
    main()