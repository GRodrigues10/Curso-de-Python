lista = list()
while True:
    numero = int(input('Digite valores para a lista:'))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Esse número já existe...\nDigite outro!')

    continuar = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção Inválida!')
        continuar = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Lista De Números: {sorted(lista)}')
print('Fim do Programa!')

