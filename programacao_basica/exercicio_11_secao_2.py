def ler_valores():
    velocidade_media = float(input('velocidade_media durante a viagem: '))
    tempo_gasto = float(input('tempo de gasto na viagem: '))
    return velocidade_media, tempo_gasto

def calculo_distancia(velocidade, tempo):
    distancia = velocidade * tempo
    return distancia

def calculo_quantidade_litros(distancia):
    quantidade_litros = distancia / 12
    return quantidade_litros

def resultado(velocidade, tempo, distancia, quantidade_litros):
    print(f'A distancia percorrida foi de {distancia:.2f}km')
    print(f'A quantidade de litros percorrida foi de {quantidade_litros:.2f}L')
    print(f'A velocidade média durante a viagem foi de {velocidade:.2f}km/h')
    print(f'O tempo de gasto na viagem foi de {tempo:.2f} hora(s)')

def main():
    velocidade, tempo = ler_valores()
    distancia = calculo_distancia(velocidade, tempo)
    quantidade_litros = calculo_quantidade_litros(distancia)
    resultado(velocidade, tempo, distancia, quantidade_litros)
    
if __name__ == '__main__':
    main()