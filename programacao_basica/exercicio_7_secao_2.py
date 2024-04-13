def sum_list(list):
    soma = 0
    for i in range(len(list)):
        soma += list[i]
    print(soma)
def main():
    list = []
    for i in range(0,6):
        list.append(int(input(f"Digite o numero {i+1}: ")))
    sum_list(list)
    
if __name__ == "__main__":
    main()