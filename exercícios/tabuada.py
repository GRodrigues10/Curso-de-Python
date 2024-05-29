n = int(input('Digite um número para calcular a tabuada:'))
mult = 0
op = 0
for c in range(1, 11):
    mult = n * c
    print(f'{n} X {c} = {mult}')
while op not in 'SN':
    op = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    print('Opção Inválida! Tente Novamente!')
    if op == 'N':
        break
print('Fim do Programa!')






