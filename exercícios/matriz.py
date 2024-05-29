matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite o valor para a posição [{i}][{j}]: '))
        matriz[j].append(valor)

for linha in matriz:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()