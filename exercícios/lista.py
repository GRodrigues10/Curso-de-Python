maior = 0
menor = 0
lista = list()
for cont in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {cont}:')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f'Você digitou os valores:{lista}')
print(f'O maior valor é {maior} e ele está na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor é {menor} e ele está na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()

