def metade(numero=0):
    return numero / 2


def dobro(numero=0):
    return numero * 2


def aumentar(numero, taxa=0):
    return numero + (numero * taxa/100)


def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')





