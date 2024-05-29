print('-=' * 14)
print('* LISTA DE PARES E ÍMPARES *')
print('-=' * 14)
lista = list()
lista_par = list()
lista_impar = list()
cont_par = 0
cont_impar = 0
while True:
    v = int(input('Digite um número:'))
    lista.append(v)
    op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if v % 2 == 0:
        lista_par.append(v)
        cont_par += 1
    else:
        lista_impar.append(v)
        cont_impar += 1

    while op not in 'SN':
        print('Opção Inválida!')
        op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break
print(f'A lista completa é:{lista}')
print(f'A lista de números pares é:{lista_par}')
print(f'A lista de números ímpares é:{lista_impar}')
print('Fim do Programa!')
