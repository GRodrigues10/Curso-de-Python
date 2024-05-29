'''a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)'''

# Usando Função:


'''def soma(a, b):
    print(f'A = {a} e b = {b}')
    s = a + b
    print(f'A soma é = {s}')
'''

# Programa Principal

# Nesse caso é obrigado passar 2 parâmetros, se não, var dar erro!

'''soma(8, 9)
soma(2, 1)
soma(4, 1)'''

# Pode definir quem é o 'A' e quem é o 'B', independentemente da posição:
# soma(b=1, a=2)

# Empacotar Parâmetros:

# Esse # *num empacota vários ou 1 número.


'''def contador(*num):
    for valor in num:
        print(f' {valor} ', end='')
    print(' FIM!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 7, 2)
'''


'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 7, 2)'''


'''def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos]  *= 2
        pos += 1


valores = [4, 5, 6, 7, 8]
dobra(valores)
print(valores)'''


def soma(*num):
    s = 0
    for numero in num:
        s += numero
    print(f'Somando os valores {num} temos = {s}')


soma(5, 2)
soma(2, 9, 4)

