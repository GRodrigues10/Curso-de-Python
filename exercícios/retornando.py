import random
print('\033[1;97mPEDRA, PAPEL E TESOURA\033[m ')
print('\033[1;97mEscolha uma opção:\033[m ')
print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')
while True:
    op = str(input('Qual a sua escolha? '))
    while op not in '1 2 3':
        op = str(input('[ERRO] - Tente novamente! '))
    computador = str(random.randint(1, 3))

    if op == '1':
        op = 'Pedra'
    elif op == '2':
        op = 'Papel'
    elif op == '3':
        op = 'Tesoura'

    if computador == '1':
        computador = 'Pedra'
    elif computador == '2':
        computador = 'Papel'
    elif computador == '3':
        computador = 'Tesoura'

    print(f'Você escolheu: {op}')
    print(f'O computador escolheu: {computador}')

    if op == computador:
        print('Empate')
    elif (op == 'Pedra' and computador == 'Tesoura') or \
         (op == 'Papel' and computador == 'Pedra') or \
         (op == 'Tesoura' and computador == 'Papel'):
        print('Você ganhou!')
    else:
        print('Você perdeu!')

    cont = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if cont != 'S':
        break

