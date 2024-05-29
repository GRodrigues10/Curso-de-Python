pessoas = list()
dados = list()
maior = 0
menor = float('inf')
while True:
    dados.append(str(input('Digite o seu nome:')))
    dados.append(float(input('Digite o seu peso:')))
    op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]

    if dados[1] > maior:
        maior = dados[1]
    if dados[1] < menor:
        menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    while op not in 'SN':
        print('Opção Inválida!')
        op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break
print(f'Dados Digitados: {pessoas}.')
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas foram: ', end='')
for p in pessoas:
    if p[1] == maior:
        maior = p[1]
        print(f'[{p[0]}] ', end='')
print(f'\nAs pessoas mais leves foram: ', end='')
for p in pessoas:
    if p[1] == menor:
        menor = p[1]
        print(f'[{p[0]}] ', end='')


print('\nFim do programa!')


