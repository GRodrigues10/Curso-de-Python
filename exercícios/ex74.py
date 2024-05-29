import random
'''maior = 0
menor = float('inf')
    n = (random.randint(1, 10))
    tupla = n
    print(f' {tupla} ', end='')
    if tupla > maior:
        maior = tupla
    elif tupla < menor:
        menor = tupla

print(f'\n\nO maior valor é {maior}')
print(f'O menor valor é {menor}')
'''

#Outra forma de fazer:
n = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
     random.randint(1, 10), random.randint(1, 10))
print('Os valores Sorteados foram:')
for numero in n:
    print(f'{numero} ', end='')
print(f'\nO maior valor é: {max(n)}')
print(f'O menor valor é: {min(n)}')

