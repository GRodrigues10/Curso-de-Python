# * TUPLAS *
#Tuplas são imutáveis.
'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-2:])
#forma 1:
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra kct kkkkkkkkkkkkk')


print(len(lanche))#ver quantos itens tem na tupla.
#forma 2:
for cont in range(0, len(lanche)):
    print(lanche[cont])# mode de fazer usando o range
    print(f'Eu vou comer {comida} na posição {cont}')

#enumerando o lanche da forma 1:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra kct kkkkkkkkkkkkk')'''

'''lanche = ('Hambúrguer', 'Batata Frita', 'Pizza', 'Pudim')
print(sorted(lanche))# O sorted coloca em ordem alfabética.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))#Len mostra o tamnho, a quantidade de elementos.
print(c.count(5))#Count conta quantas vezes aparece o número 5.
print(c.index(8))#Index mostra a posição que está o 8.
print(c.index(5, 2))#começando a contar da posição 2.'''

pessoa = ('Gustavo', 39, 'M', 99.88)#Tuplas aceitam vários tipos de dados.
print(pessoa)

#dell pessoa - Serve para apagar uma variável, nesse caso a variável 'pessoa'.