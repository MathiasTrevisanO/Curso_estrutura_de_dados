
def calculo_distancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia

def litros_utilizados(distancia):
    litros = distancia / 12
    return litros

def main():
    tempo = float(input('Digite o tempo gasto na viagem: '))
    velocidade = float(input('Digite a velocidade média durante a viagem: '))
    distancia = calculo_distancia(tempo, velocidade)
    print(f'A distância é de {distancia:.2f}m')
    litros = litros_utilizados(distancia)
    print(f'A quantidade de litros utilizados é de {litros:.2f}L')
    
if __name__ == '__main__':
    main()