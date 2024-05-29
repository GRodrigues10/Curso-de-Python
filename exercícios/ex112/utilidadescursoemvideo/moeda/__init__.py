def aumento(n=0, r=False):
    preco = n + (n * 0.10)
    if r:
        return f'R${preco:.2f}'.replace('.', ',')
    else:
        return preco


def diminuir(n=0, r=False):
    preco = n - (n * 0.13)
    if r:
        return f'R${preco:.2f}'.replace('.', ',')
    else:
        return preco


def dobro(n=0, r=False):
    preco = n * 2
    if r:
        return f'R${preco:.2f}'.replace('.', ',')
    else:
        return preco


def metade(n=0, r=False):
    preco = n / 2
    if r:
        return f'R${preco:.2f}'.replace('.', ',')
    else:
        return preco


def formatacao(n=0):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR:'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{formatacao(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Aumento em 10%: \t{aumento(preco, True)}')
    print('-' * 30)
