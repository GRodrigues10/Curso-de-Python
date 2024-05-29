'''def notas():
    lista = list()
    cont = 1
    while True:
        dicionario = dict()
        dicionario['nome'] = str(input(f'Digite o nome do aluno {cont}:'))
        dicionario['nota1'] = float(input(f'Digite a primeira nota do aluno {dicionario["nome"]}:'))
        dicionario['nota2'] = float(input(f'Digite a segunda nota do aluno {dicionario["nome"]}:'))
        lista.append(dicionario)
        cont += 1
        op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
        while op not in 'SN':
            print('Tente Novamente!')
            op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
        if op == 'N':
            break

    max_nome_length = max(len(aluno['nome']) for aluno in lista)

    # Imprimir os cabeçalhos das colunas
    print(f'{"Nome":<{max_nome_length + 2}}{"Nota1":<8}{"Nota2":<8}{"Média":<8}{"Situação":<8}')

    # Imprimir os dados formatados
    for aluno in lista:
        nome = aluno["nome"]
        nota1 = aluno["nota1"]
        nota2 = aluno["nota2"]
        media = (nota1 + nota2) / 2

        situacao = 'Aprovado' if media >= 6 else 'Reprovado'

        print(f'{nome:<{max_nome_length + 2}}{nota1:<8.2f}{nota2:<8.2f}{media:<8.2f}{situacao:<10}')


notas()'''


# Fazendo da maneira do professor:


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou várias notas dos alunos.
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação da turma.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] > 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


resp = notas(5.5, 10, 10, 8.5, sit=True)
print(resp)
help(notas)

