import random
from time import sleep


def menu():
    titulo = '\033[1;31;40m* PEDRA, PAPEL E TESOURA *\033[m'

    print('\033[1;34m-=\033[m' * 50)
    print(titulo.center(113))
    print('\033[1;34m-=\033[m' * 50)
    print()


def cod():
    while True:
        escolha = str(input('\033[1;97m<Aperte 1 para iniciar o jogo> ou <Aperte 0 para encerrar o jogo>\033[m')).strip()

        while escolha not in '1 0' or escolha == '':
            print('\033[4;31m[ERRO!] - Opção inválida!\033[m')
            escolha = str(input('\033[1;97m<Aperte 1 para iniciar o jogo> ou <Aperte 0 para encerrar o jogo>\033[m'))

        if escolha == '0':
            break
        print()
        print('\033[1;33mOlá,\nme chamo Biru Biru e quero jogar pedra, papel e tesoura com você!'
              '\nSerá que você consegue me derrotar?\033[m')
        print()
        print('\033[4;97mOPÇÕES:\033[m')
        print()
        print('\t\033[1;33m[1]\033[1;34m - Pedra\033[m')
        print('\t\033[1;33m[2]\033[1;34m - Papel\033[m')
        print('\t\033[1;33m[3]\033[1;34m - Tesoura\033[m')
        print()

        jogador = str(input('\033[1;97mQual a sua Escolha?\033[m')).strip()
        while jogador != '1' and jogador != '2' and jogador != '3' and jogador == '':
            print('\033[4;31m[ERRO] - Opção Inválida\033[m')
            jogador = str(input('\033[1;97mQual a sua Escolha?\033[m')).strip()

        print('\033[1;33mPedra\033[m')
        sleep(1)
        print('\033[1;34mPapel\033[m')
        sleep(1)
        print('\033[1;31mTesoura\033[m')
        sleep(1)

        computador = random.randint(1, 3)

        if jogador == '1':
            jogador = 'Pedra'
        elif jogador == '2':
            jogador = 'Papel'
        elif jogador == '3':
            jogador = 'Tesoura'

        if computador == 1:
            computador = 'Pedra'
        elif computador == 2:
            computador = 'Papel'
        elif computador == 3:
            computador = 'Tesoura'

        if jogador == computador:
            print(f'\033[1;97mVocê escolheu {jogador} e o Biru Biru escolheu {computador}.\033[m')
            print('\033[34mEmpate!\033[m')

        elif (jogador == 'Pedra' and computador == 'Tesoura') or (jogador == 'Papel' and computador == 'Pedra') or (
                jogador == 'Tesoura' and computador == 'Papel'):
            print(f'\033[1;97mVocê escolheu {jogador} e a máquina escolheu {computador}.\033[m')
            print('\033[1;33mVocê Venceu!\033[m')
        else:
            print(f'\033[1;97mVocê escolheu {jogador} e a máquina escolheu {computador}.\033[m')
            print('\033[1;31mVocê Perdeu!\033[m')

    print('\033[1;31mFim de Jogo!\033[m')