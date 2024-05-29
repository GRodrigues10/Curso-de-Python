import random
import time

numero = []


def sorteia():
    print('Sorteando 5 valores:')
    for c in range(1, 6):
        time.sleep(0.5)
        n = random.randint(1, 10)
        numero.append(n)
        print(f' {n} ', end='')


def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma


sorteia()
print(f'\nA soma dos números pares de {numero} é {soma_pares(numero)}.')
