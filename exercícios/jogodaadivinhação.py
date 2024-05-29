import random

print('-=' * 30)
print('{:^60}'.format('* JOGO DA ADIVINHAÇÃO *'))
print('-=' * 30)
nome = str(input('Qual é o seu nome? '))
print(f'Olá {nome}, me chamo Sat e tenho um desafio para você...')
print('Estou pensando em um número entre 0 e 10.')
print('Você consegue adivinhar?')

computador = random.randint(0, 10)
tentativas = 3

while tentativas > 0:
    op = int(input('Digite um número entre 0 e 10: '))

    if op < computador:
        print('O número que estou pensando é maior. Tente novamente.')
    elif op > computador:
        print('O número que estou pensando é menor. Tente novamente.')
    else:
        print('Parabéns! Você acertou!')
        break

    tentativas -= 1

if tentativas == 0:
    print(f'Você usou todas as tentativas. O número que eu estava pensando era {computador}.')