'''cont = 0
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um número:'))
n4 = int(input('Digite o último número:'))
tupla = (n1, n2, n3, n4)
print(tupla)
numero_frequente = max(set(tupla), key=tupla.count)
print(f'O número mais repetido na tupla é {numero_frequente}')
print(f'O número {n2} apareceu na posição {tupla.index(n2)}.')

print("Números pares na tupla:")
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end='')
'''
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um número:'))
n4 = int(input('Digite o último número:'))
tupla = (n1, n2, n3, n4)
print(tupla)
numero_frequente = tupla.count(9)
print(f'O número 9 apareceu {numero_frequente} vezes.')
print(f'O número 3 apareceu na posição {tupla.index(3)}.')

print("Números pares na tupla:")
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end='')
