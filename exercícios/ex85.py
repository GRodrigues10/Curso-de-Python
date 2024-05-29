lista = [[], []]
for c in range(1, 8):
    v = int(input(f'Digite o número {c}:'))
    if v % 2 == 0:
        lista[0].append(v)
    else:
        lista[1].append(v)
print(f'A lista completa em ordem crescente é: {sorted(lista)}')
print(f'A lista com números pares em ordem crescente é: {sorted(lista[0])}')
print(f'A lista com números ímpares em ordem crescente é: {sorted(lista[1])}')

