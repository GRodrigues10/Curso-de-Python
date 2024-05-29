# Programa não está pronto ainda...
lista = list()


def alunos():
    while True:
        dicionario = dict()
        dicionario['nome'] = str(input('Digite o nome do aluno:'))
        dicionario['nota 1'] = float(input(f'Digite a primeira nota do {dicionario["nome"]}:'))
        dicionario['nota 2'] = float(input(f'Digite a segunda nota do {dicionario["nome"]}:'))
        lista.append(dicionario)
        op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
        while op not in 'SN':
            print('Tente Novamente!')
            op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
        if op == 'N':
            break

    for pos, aluno in enumerate(lista):
        print(f'Aluno {pos + 1}: {aluno["nome"]} {aluno["nota 1"]} {aluno["nota 2"]}')


# Programa Principal:
alunos()