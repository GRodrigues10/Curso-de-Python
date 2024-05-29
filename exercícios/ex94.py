cadastros = []
cont = 0
soma_idade = 0
mulheres = []  # Lista para armazenar nomes das mulheres

while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]

    while pessoa['sexo'] not in 'MF':
        print('Erro! Só existem 2 sexos!\nDigite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]

    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']

    cont += 1

    if pessoa['sexo'] == 'F':  # Modificação para contar mulheres
        mulheres.append(pessoa['nome'])

    cadastros.append(pessoa)

    op = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if op != 'S':
        break

print(f'Ao todo foram cadastradas {cont} pessoas.')
if len(mulheres) > 0:
    print(f'As mulheres cadastradas foram: {", ".join(mulheres)}.')
else:
    print('Nenhuma mulher foi cadastrada.')

media_idade = soma_idade / cont
print(f'A média das idades é: {media_idade:.1f}')

print('Pessoas com idade acima da média:')
for pessoa in cadastros:
    if pessoa['idade'] > media_idade:
        print(pessoa['nome'])
