from datetime import datetime
dicionario = dict()
dicionario['nome'] = str(input('Nome:'))
ano_nascimento = int(input('Ano de Nascimento:'))
dicionario['idade'] = datetime.now().year - ano_nascimento
dicionario['ctps'] = int(input('Carteira de Trabalho [0 se não tem]:'))
print('\033[1;97m-=\033[m' * 30)
if dicionario['ctps'] == 0:
    for k, v in dicionario.items():
        print(f'O {k} é igual a:{v}')
else:
    dicionario['contratação'] = int(input('Ano de Contratação:'))
    dicionario['salário'] = float(input('Salário:R$'))
    dicionario['aposentadoria'] = dicionario['contratação'] - ano_nascimento + 35

    for chave, valor in dicionario.items():
        print(f'O {chave} é igual a:{valor}')


