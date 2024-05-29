''' teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)


galera = list()
teste[0] = 'Gabriel'
teste[1] = 22
galera.append(teste[:])
print(galera) '''

# MEXENDO EM LISTA DENTRO DE LISTA

'''galera = [['Gabriel', 19], ['João', 43], ['Lucas', 32], ['José', 34]]
print(galera[0][0])
print(galera[1][1])
print(galera[2][1])'''
'''galera = [['Gabriel', 19], ['João', 43], ['Lucas', 32], ['José', 34]]
for pessoa in galera:
    #print(pessoa)
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')'''

# FAZENDO UMA CÓPIA DE UMA LISTA:
galera = list()
dado = list()

'''for c in range(0, 4):
    dado.append(str(input('Digite o seu nome:')))
    dado.append(int(input('Digite a sua idade:')))
    galera.append(dado[:])
    dado.clear()
print(galera)'''

maior = 0
menor = 0

for c in range(0, 4):
    dado.append(str(input('Digite o seu nome:')))
    dado.append(int(input('Digite a sua idade:')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maior e {menor} menor.')

