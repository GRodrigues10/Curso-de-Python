def area():
    largura = float(input('Largura (m):'))
    comprimento = float(input('Comprimento (m):'))
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é:{a}m².')


def linha():
    print('\033[1;97m-\033[m' * 30)


print('\033[1;97m{:^33}'.format('Controle de Terrenos\033[m'))
linha()
area()
