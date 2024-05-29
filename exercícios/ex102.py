'''def fatorial(n):
    fat = 1
    for c in range(n, 0, -1):
        fat = fat * c
        print(f'{c} x ', end='')
    return fat


numero = int(input('Digite um número para calcular o fatorial:'))
fator = fatorial(numero)
print(f'\nO fatorial de {numero} é {fator}')'''


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional - Mostrar ou não a conta).
    :return: Retorna o fatorial de um número.





    """
    fat = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        fat = fat * c
    return fat


print(fatorial(5, show=True))
help(fatorial)


