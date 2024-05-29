import time
import random

print('\033[1m-\033[m' * 30)
print('\033[1;97m{:^30}\033[m'.format('JOGO NA MEGA SENA'))
print('\033[1m-\033[m' * 30)

jogo = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(jogo):
    lista = []
    print(f'Jogo {j + 1}: [', end='', flush=True)

    sort = random.sample(range(1, 62), 6)

    for i in range(6):
        lista.append(sort[i])
        print(sort[i], end='')
        if i < 5:
            print(', ', end='', flush=True)
        else:
            print(']', end='', flush=True)
        time.sleep(0.5)
    print()
print('\033[1;97m--------< BOA SORTE! >--------\033[m')

