import random
import time

print('\033[1;30m-=\033[m' * 30)
print('\033[1;97m{:^65}'.format('* PEDRA, PAPEL E TESOURA *\033[m'))
print('\033[1;30m-=\033[m' * 30)

print('\033[1;34mEscolha uma opção:\033[m')
print('\033[1;32m[1] - Pedra\033[m')
print('\033[1;32m[2] - Papel\033[m')
print('\033[1;32m[3] - Tesoura\033[m')
while True:
    jogador = int(input('\033[1;36mQual é a sua escolha?\033[m'))
    computador = random.randint(1, 3)

    while jogador != 1 and jogador != 2 and jogador != 3:
        print('\033[1;31mOpção Inválida!\033[m')
        jogador = int(input('\033[1;36mQual é a sua escolha?\033[m'))
    j = 0
    c = 0
    if jogador == 1:
        j = 'Pedra'
    elif jogador == 2:
        j = 'Papel'
    elif jogador == 3:
        j = 'Tesoura'

    if computador == 1:
        c = 'Pedra'
    elif computador == 2:
        c = 'Papel'
    elif computador == 3:
        c = 'Tesoura'
    print('Pedra')
    time.sleep(1)
    print('Papel')
    time.sleep(1)
    print('e Tesoura....')
    time.sleep(1)
    print(f'\033[1;97mVocê escolheu {j} e o computador escolheu {c}.\033[m')
    if jogador == computador:
        print('\033[1;352mEmpate!\033[m')

    elif jogador == 1 and computador == 3 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
        print('\033[1;32mVocê Venceu!\033[m')
    else:
        print('\033[1;31mVocê Perdeu!\033[m')

    conti = str(input('\033[1;32mDeseja Continuar?[S/N]\033[m')).strip().upper()[0]
    while conti not in 'SN':
        print('\033[1;31mOpção Inválida!\033[m')
        conti = str(input('\033[1;32mDeseja Continuar?[S/N]\033[m')).strip().upper()[0]
    if conti == 'N':
        break
print('\033[1;97m\nFim do Programa!\033[m')
print('\033[1;34m-=\033[m' * 30)
