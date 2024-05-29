matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = 0
pares = 0
soma = 0
soma3 = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um número para a posição [{i} {j}]:'))
        if matriz[i][j] % 2 == 0:
            cont = cont + 1
            soma = soma + matriz[i][j]
# A linha varia, porém a coluna sempre será 2 por isso a linha varia e a coluna é fixa no 2.
for linha in range(0, 3):
    soma3 += matriz[linha][2]
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

print('-=' * 30)
print(f'Existem {cont} números pares e a soma deles é {soma}.')
print(f'O maior valor da segundo linha é: {max(matriz[1])}')
print(f'A soma dos valores da terceira coluna é: {soma3}')


