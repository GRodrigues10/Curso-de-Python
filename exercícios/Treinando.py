from random import randint
print('=' * 23)
print('* Jogo da Adivinhação *')
print('=' * 23)
tentativas = 1

print('Olá humano!\nEstou pensando em um número de 1 a 5.\nVocê consegue adivinhar?')
while True:
    num = int(input('Escolha um número entre 1 e 5:'))
    computador = randint(1, 5)
    if num == computador:
        print(f'Você acertou! Eu estava pensando no número {computador}\nVocê acertou em {tentativas} tentativas')
        break
    else:
        print(f'Você errou! você possui ({tentativas} / 3) tentativas.')

    tentativas += 1

    if tentativas > 3:
        print('Game Over!')
        break


