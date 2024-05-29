# A função help() te explica as coisas que tem no python.
# Isso pode ser feito pelo console ou pelo próprio python.

''' print('Olá Mundo!')
help(print) '''  # Explicando para que serve o print.

# Outra maneira fazer: Não é necessariamente igual o doc.
'''print(input.__doc__)'''

# Docstrings:

'''def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno

    * Função criada pelo gabrielzin do pneu em 2023. *
    """

   c = i
    while i <= f:
        print(f'{c}', end='')
        c += p
    print('Fim!')
help(contador)'''

# Parâmetros Opcionais:

# Nos parâmetros opcionais você pode ter parâmetros à mais e não mesmo assim não dá problema.
# Mas para isso tem que colocar a variável do parâmetro igual a 0 ou qualquer outro valor.


'''def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 4, 5)
somar(3, 4)'''


# Escopo de variáveis:

# Existe 2 tipos de escopos: Global e Local. Global funciona em
# todo o programa, local funciona só na função.

'''
def funcao():
    n1 = 4 #LOCAL
    print(f'N1 dentro vale {n1}')


n1 = 6 #GLOBAL
funcao()
print(f'N1 fora vale {n1}')

# É possível fazer uma variável ser global digitando a palavra 'global' antes da variável.

'''

# Retornando Valores


'''def somar(a, b, c=0):
    s = a + b + c
    return s


r1 = somar(3, 4, 5)
r2 = somar(3, 4)
print(f'As soma valem {r1} e {r2}.')'''


'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número:'))
print(f'O fatorial de  {n} é igual a {fatorial(n)}.')'''


def par(num=0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número:'))
if par(n):
    print('É par!')
else:
    print('É ímpar!')




