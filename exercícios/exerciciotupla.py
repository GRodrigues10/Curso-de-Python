# Exercício 1:
'''tupla = ('Python', 50, False, 100.75)
print(tupla)
print('\n')
for item in tupla:
    print(item)'''


# Exercício 2:
'''numero = (1, 4, 9, 2, 5, 3)
print(numero[4])'''


# Exercício 3:
'''numero = (1, 4, 9, 2, 5, 3)
print(numero[1])
print(numero[2])
print(numero[3])'''


# Exercício 4:

'''numero = (1, 2, 3, 4, 5)
print(numero[::-1])'''



# Exercício 5:
'''n = (1, 3, 5, 6, 3, 6, 7, 3)
cont = n.count(3)
print(f'O número 3 aparece {cont} vezes.')'''


# Exercício 6:
'''soma = 0
n = (1, 3, 5, 6, 3, 6, 7, 3)
for numero in n:
    soma = soma + numero
print(f'A soma dos números da tupla é {soma}')

# Maneira safada de fazer:
print(sum(n))'''

# Exercício 7:

'''n = (1, 3, 5, 6, 3, 6, 7, 3, 9)
for item in n:
    if item == 9:
        print('Sim')
        break
else:
    print('Não')

# Maneira safada de fazer:
print(9 in n)'''

# Exercício 8:

'''tupla_abc = (1, 2, 3)
a, b, c = tupla_abc
print(c)'''
