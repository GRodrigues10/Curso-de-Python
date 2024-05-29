from random import randint
print('=' * 24)
print('* Jogo da Adivinhação *')
print('=' * 24)
while True:
    tentativas = 0
    print('Estou pensando em um número entre 0 e 5. \nVocê consegue adivinhar?')
    computador = randint(0, 5)
    while tentativas < 3:
        palpite = int(input('Seu Palpite:'))
        if computador > palpite:
            print('Estou pensando em um número maior.')

        elif computador < palpite:
            print('Estou pensando em um número menor.')

        elif palpite == computador:
            print(f'Você acertou! Eu estava pensando no número {computador}')
            break

        tentativas += 1

    if tentativas == 3:
        print(f'Você perdeu! Eu estava pensando no número {computador}')
    novamente = str(input('Deseja Jogar novamente?'))
    if novamente.lower() != 's':
        break

