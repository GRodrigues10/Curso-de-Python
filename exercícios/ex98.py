from time import sleep


def contagem():
    for c in range(1, 11):
        sleep(0.5)
        print(f' {c} ', end='')


def regressiva():
    for r in range(10, -1, - 2):
        sleep(0.5)
        print(f' {r} ', end='')


def user():
    i = int(input('Início:'))
    f = int(input('Final:'))
    p = int(input('Passo:'))

    if i > f:
        p = -1
    else:
        p = 1
    print(f'Contagem de {i} até {f} contando de {p} em {p}:')
    for d in range(i, f, p):
        sleep(0.5)
        print(f' {d} ', end='')


# Programa Principal:

print('-' * 40)
print('Contagem de 1 até 10 contando de 1 em 1:')
contagem()
print('\nContagem regressiva de 10 até 0 contando de 2 em 2:')
regressiva()
print('\nAgora é a sua vez de escolher a contagem:')
user()

