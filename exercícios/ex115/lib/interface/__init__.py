def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero

        except (ValueError, TypeError):
            print('\033[4;31m[ERRO] - Tivemos um problema com os tipos de dados que você digitou!\033[m')

        except KeyboardInterrupt:
            print('Erro na entrada de dados interrompida pelo usuário.')
            return 0


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leia_int('\033[97mSua Opção:\033[m')
    return opc
