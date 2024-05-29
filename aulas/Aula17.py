# LISTAS:

# Listas são mutáveis.
'''num = [2, 4, 5]
print(num)
# Adicionando valores na lista:
num.append(1)
print(num)
# Ordenando valores na lista:
num.sort()
print(num)
# Ordenando valores na lista de forma inversa:
num.sort(reverse=True)
print(num)
# Verificando o tamanho da lista:
print(f'Essa lista tem {len(num)} elementos.')
# Inserindo Valores na lista:
# Inserindo o valor 0 na posição 2:
num.insert(2, 0)
print(num)

# Removendo elementos de uma lista:
# O pop elemina o último elemento da lista, porém pode ser usado para eliminar qualquer elemento.
num.pop()
print(num)
# Removendo o número 4, o método remove elimina os números a partir do próprio número.
num.remove(4)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 5.')'''

'''valores = list()
valores.append(5)
valores.append(4)
valores.append(9)
for valor in valores:
    print(f'{valor}...', end='')

print('\n')'''

# Esse for mostra a posição e o valor encontrado.
'''for c, valor in enumerate(valores):
    print(f'Na posição {c} encontre o valor:{valor}.')'''

# Lendo valores pelo teclado e colocando na lista:
'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))

for c, valor in enumerate(valores):
    print(f'Na posição {c} encontre o valor:{valor}.')'''

# QUANDO VOCÊ IGUALA UMA LISTA NA OUTRA, O PYTHON CRIA UMA LIGAÇÃO ENTRE ELA.
'''a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'A lista  A é:{a}')
print(f'A lista  B é:{b}')'''

#FAZENDO UMA CÓPIA DE UMA LISTA:
a = [2, 3, 4, 7]
b = a[:]
b[2] = 6
print(f'A lista  A é:{a}')
print(f'A lista  B é:{b}')

