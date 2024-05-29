from random import randint

print('* \033[97m Pedra, Papel e Tesoura * \033[m')

while True:
    print('Escolha uma opção:')
    print('[1] - Pedra')
    print('[2] - Papel')
    print('[3] - Tesoura')
    jogador = str(input('Qual a sua escolha?'))
    computador = randint(1, 3)

    while jogador not in '1 2 3':
        print('Opção Inválida!')
        jogador = str(input('Tente Novamente:'))

    if jogador == '1':
        print('Pedra!')

    if jogador == '2':
        print('Papel!')

    if jogador == '3':
        print('Tesoura!')

    if computador == '1':
        print('Pedra!')

    if computador == '2':
        print('Papel!')

    if computador == '3':
        print('Tesoura!')

    print(f'Computador escolheu {computador}')

    if jogador == str(computador):
        print('Empate')
    elif jogador == '1' and computador == 2:
        print(f'Você Perdeu! O computador escolheu {computador} e você {jogador}')
    elif jogador == '3' and computador == 1:
        print(f'Você Perdeu! O computador escolheu {computador} e você {jogador}')
    elif jogador == '2' and computador == 3:
        print(f'Você Perdeu! O computador escolheu {computador} e você {jogador}')
    else:
        print(f'Você Ganhou! O computador escolheu {computador} e você {jogador}')