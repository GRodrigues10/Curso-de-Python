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


def leia_float(num):
    while True:
        try:
            numero = float(input(num))
            return numero

        except (ValueError, TypeError):
            print('\033[4;31m[ERRO] - Tivemos um problema com os tipos de dados que você digitou!\033[m')


        except KeyboardInterrupt:
            print('Erro na entrada de dados interrompida pelo usuário.')
            return 0


n_int = leia_int('Digite um número inteiro:')
n_float = leia_float('Digite um número flutuante:')

print(f'\033[1;33mVocê digitou o número inteiro {n_int}.\033[m')
print(f'\033[1;34mVocê digitou o número flutuante {n_float}.\033[m')
