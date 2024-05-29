def leia_inteiros(num):
    while True:
        numero = str(input(num))
        if numero.isnumeric():
            return numero
        else:
            print('Opção Inválida! Tente Novamente...')


n = leia_inteiros('Digite um número:')
print(f'Você digitou o número {n}.')
