from time import sleep

c = ['\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m']


def ajuda(com):
    titulo(f'Acessando o manual do comando {com}...', 3)
    sleep(2)
    print(c[2], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''

while True:
    sleep(0.5)
    titulo('SISTEMA DE AJUDA PyHELP', 4)

    comando = str(input('\033[1;97;40mFunção ou Biblioteca:\033[m'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 2)

