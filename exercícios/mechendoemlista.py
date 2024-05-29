lista = list()
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while op not in 'SN':
        print('Essa opção é inválida, ANIMAL!')
        op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break
print(lista)
while True:
    delete = str(input('Deseja excluir algum número da lista? [S/N]')).strip().upper()[0]
    if delete == 'N':
        break

    else:
        op = int(input('Qual número você deseja excluir?'))

        while op not in lista:
            print('Opção Inválida!')
            op = int(input('Qual número você deseja excluir?'))
        lista.remove(op)
        print(lista)

print('Fim do Programa!')