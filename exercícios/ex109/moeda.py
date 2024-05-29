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