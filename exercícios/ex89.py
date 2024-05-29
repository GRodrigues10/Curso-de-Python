while True:
    lista = []
    cont = 0
    while True:
        alunos = []
        nome = input('Nome: ')
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))

        alunos.append(nome)
        alunos.append(n1)
        alunos.append(n2)

        lista.append(alunos)

        cont += 1
        op = input('Deseja Continuar? [S/N]: ').strip().upper()
        while op not in 'SN':
            print('Opção Incorreta!')
            op = input('Deseja Continuar? [S/N]: ').strip().upper()
        if op == 'N':
            break

    # Exibindo posição, nome, notas originais, soma das notas e média das notas com linha vertical
    print('POSIÇÃO  | NOME    | NOTA 1 | NOTA 2 | SOMA DAS NOTAS | MÉDIA DAS NOTAS')
    for i, aluno in enumerate(lista, start=1):
        nome = aluno[0]
        nota1, nota2 = aluno[1], aluno[2]  # Pegando as notas individualmente
        soma_notas = sum(aluno[1:])  # Somando as notas
        media = soma_notas / 2  # Calculando a média corretamente

        # Formatando a exibição com linha vertical
        print(f'{i:<8} | {nome:<7} | {nota1:<6.1f} | {nota2:<6.1f} | {soma_notas:<14.1f} | {media:<6.1f}')

    continuar = int(input('Deseja Mostrar a nota de qual aluno? Digite o número do aluno (ou 999 para parar): '))
    if continuar == 999:
        break
    elif continuar <= len(lista) and continuar > 0:
        aluno_selecionado = lista[continuar - 1]
        print(f'Notas do Aluno {continuar}: {aluno_selecionado[1]} e {aluno_selecionado[2]}')
    else:
        print('Número de aluno inválido. Tente novamente.')