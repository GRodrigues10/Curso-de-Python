maior = 0
menor = float('inf')
lista = list()
for cont in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {cont}:')))

for item in lista:
    if item > maior:
        maior = item
    if item < menor:
        menor = item
print('\n')
print(f'Você digitou os valores:{lista}')
print(f'O maior valor é {maior} e ele está na posição {lista.index(maior)}.')
print(f'O menor valor é {menor} e ele está na posição {lista.index(menor)}.')
