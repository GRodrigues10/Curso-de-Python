from time import sleep


def calculadora(comando):
    while True:
        cont = 1
        for c in range(1, 11):
            cont += 1
            mult = comando * c
            print(f'{comando} x {c} = {mult}')

        op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]

        while op not in 'SN':
            print('Tente Novamente!')
            op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
        if op == 'N':
            break
        else:
            comando = int(input('Digite um número:'))


# Programa Principal:
print('\033[0;31;40m=\033[m' * 110)
print('\033[1;97m{:^110}'.format('* CALCULADORA * \033[m'))
print('\033[0;31;40m=\033[m' * 110)

com = int(input('Digite um número:'))
calculadora(com)
print('FINALIZANDO...')
sleep(2)

