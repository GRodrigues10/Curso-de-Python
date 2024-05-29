n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))
n4 = int(input('Digite um número:'))

tupla = (n1, n2, n3, n4)
print(tupla)
numero_frequente = max(set(tupla), key=tupla.count)
print(numero_frequente)
for c in tupla:
    if c % 2 == 0:
        print(c,end='')

