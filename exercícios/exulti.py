print('\033[30m===\033[m' * 10)
print('{:^40}'.format('\033[1;97m* BANCO DO BRASIL *\033[m'))
print('\033[30m===\033[m' * 10)

valor = int(input('Qual será o valor a ser sacado?'))
caixa = 20, 50, 30, 1
total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total = total - ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break

