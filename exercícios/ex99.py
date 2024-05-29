from time import sleep


# Função Linha:
def linha():
    print('\033[1;97m-=\033[m' * 30)


# Função Maior:
def maior(*num):
    cont = 0
    sleep(0.5)
    print('\033[1;34mAnalisando os valores informados...\033[m')
    print('\033[1;31mOs valores informados foram:\033[m', end='')
    for i in num:
        sleep(0.5)
        print(f'\033[1;33m {i}\033[m ', end='')
        cont += 1
    print()
    print(f'\033[1;36mForam informados ao todo {cont} valores\033[m')

    print(f'\033[1;97mO maior valor é: {max(num)}\033[m')


# Programa Principal:
linha()
maior(3, 4, 5, 6, 7, 3)
linha()
maior(5, 6, 3)
linha()
maior(8, 6, 5)
linha()

