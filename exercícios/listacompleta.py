print('\033[1;30m=\033[m' * 100)
print('\033[1;97m{:^95}'.format('* ADICIONE NÚMEROS NA LISTA *\033[m'))
print('\033[1;30m=\033[m' * 100)
lista_num = list()
while True:
    valor = int(input('\033[1;97mDigite um número para colocar na lista:\033[m'))
    if valor in lista_num:
        print('\033[3;31mERRO!!! Esse número ja foi adicionado na lista!\033[m')
        print('\033[3;31mPor favor, insira outro número!😁👍\033[m')

    else:
        lista_num.append(valor)

    continuar = str(input('\033[1;33mDeseja adicionar mais números na lista? [S/N]\033[m')).strip().upper()[0]

    while continuar not in 'SN':
        print('\033[3;31mOpção Inválida! Tente Novamente!\033[m')
        continuar = str(input('\033[1;33mDeseja adicionar mais números na lista? [S/N]\033[m')).strip().upper()[0]
    if continuar == 'N':
        break
print('\n')

print(f'\033[1;97mA lista de números em Ordem Crescente ficou assim: {sorted(lista_num)}\033[m')
print('\033[1;36m-=\033[m' * 70)
