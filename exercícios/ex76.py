print('\033[36m=\033[m' * 50)
print('\033[1;97m{:^52}'.format('LISTAGEM DE PREÇOS\033[m'))
print('\033[36m=\033[m' * 50)
'''tupla = ('Lápis', '.' * 30, 'R$', 30)
print(tupla)'''

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Compasso', 9.99)

for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<40}', end='')
    else:
        print(f'R${listagem[item]:>6.2f}')
