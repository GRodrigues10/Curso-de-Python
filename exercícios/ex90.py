cadastro = dict()
'''
cadastro['nome'] = str(input('Digite um nome:'))
cadastro['nota1'] = float(input('Digite a primeira nota:'))
cadastro['nota2'] = float(input('Digite a segunda nota:'))
print(f'O nome é {cadastro["nome"]}')
media = (cadastro['nota1'] + cadastro['nota2']) / 2
print(f'A média é:{media}')
if media < 6:
    print('REPROVADO!')
else:
    print('APROVADO!')'''

cadastro['nome'] = str(input('Digite um nome:'))
cadastro['média'] = float(input(f'Media de {cadastro["nome"]}:'))

if cadastro['média'] >= 6:
    cadastro['situação'] = 'APROVADO!'
elif cadastro['média'] < 6:
    cadastro['situação'] = 'RECUPERAÇÃO!'
else:
    cadastro['situação'] = 'REPROVADO!'

print(cadastro)

for i, j in cadastro.items():
    print(f'-{i} é igual a {j}')
