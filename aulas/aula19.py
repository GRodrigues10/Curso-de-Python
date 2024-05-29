# DICIONÁRIO:
# values() - Pega somente os valores. ex = Gabriel, 18.
# Keys() - Pega somente as chaves. ex = Nome, Idade.
# items() - Pega tudo. Nome:Gabriel, Idade:18.

#pessoas = {'nome': 'Gabriel', 'sexo': 'M', 'idade': 22}

'''print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''
'''for k in pessoas.keys():
    print(k,)

print('\n')

for v in pessoas.values():
    print(v,)

print('\n')

for k, v in pessoas.items():
    print(f'{k} = {v}')
    '''
# Apagando o sexo:
'''del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

# Mudando nome:
'''pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

# Adicionando peso:

'''pessoas['peso'] = 76.5
for k, v in pessoas.items():
    print(f'{k} = {v}')'''


# Criando um dicionário dentro de uma lista:
'''brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'Sp'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['UF'])
print(brasil[1]['UF'])'''

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla:'))
    brasil.append(estado.copy())
'''for estado in brasil:
    for k, v in estado.items():
        print(f'O Campo {k} tem valor {v}.')
'''

for e in brasil:
    print(e)
