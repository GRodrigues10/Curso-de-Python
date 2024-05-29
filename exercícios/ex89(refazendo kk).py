cadastro = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2

    aluno = [nome, n1, n2, media]
    cadastro.append(aluno)

    op = input('Deseja Continuar? [S/N]: ').strip().upper()
    while op not in "SN":
        print('Opção Inválida!')
        op = input('Deseja Continuar? [S/N]: ').strip().upper()
    if op == "N":
        break

print(f'{"N.":<4} {"NOME":<10} {"MÉDIA":>2}')
for i, a in enumerate(cadastro, start=1):
    print(f'{i:<4}{a[0]:<10} {a[3]:>5.1f}')  # Corrigido o índice para exibir a média

while True:
    op = int(input('Deseja ver as notas de quais alunos? (999 para interromper!): '))
    if op == 999:
        break
    if op <= len(cadastro) and op > 0:  # Verificando se a opção é válida
        print(f'Notas do aluno {cadastro[op - 1][0]} são {cadastro[op - 1][1]} e {cadastro[op - 1][2]}')
    else:
        print('Aluno não encontrado. Tente novamente!')

