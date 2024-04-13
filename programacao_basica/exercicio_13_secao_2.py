def main():
    list = []
    try:
        valor1 = float(input('valor 1:'))
        valor2 = float(input('valor 2:'))
        list.append(valor1)
        list.append(valor2)
        divide = list[0] / list[1]
    except ValueError:
        print('Valor inválido')
    except ZeroDivisionError:
        print('Não é possível dividir por 0')
    except IndexError:
        print('Valor não informado')
    except KeyboardInterrupt:
        print('O programa foi interrompido pelo usuário')
    else:
        print(f'A divisão entre {list[0]} e {list[1]} é igual a {divide:.2f}')
    
if __name__ == '__main__':
    main()