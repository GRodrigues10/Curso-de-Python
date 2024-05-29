lista = list()

while True:
    valor = (int(input('Digite valores para uma lista:')))
    if valor in lista:
        print('O valor já existe, não vou adicionar.')
    else:
        lista.append(valor)
    continuar = input('Quer continuar? [S/N]').strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = input('Quer continuar? [S/N]').strip().upper()
    if continuar == 'N':
        break

print('Programa Encerrado!')
print(f'Os valores digitados em ordem crescente foram:{sorted(lista)}')
