import time
lista = list()
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while op not in 'SN':
        print('Essa opção não existe... BURRO!')
        op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break

print('\n')

print('PROCESSANDO DADOS...')

time.sleep(2)

print('\n')

print('\033[1;97m{:^65}'.format("* LISTA *\033[m"))
print('\033[35m-=\033[m' * 30)
print(f'A lista em ordem crescente é : {sorted(lista)}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é : {lista}')
print(f'A lista possui {len(lista)} números.')
if 5 in lista:
    print(f'O número 5 existe e apareceu {lista.count(5)} vezes.')
else:
    print('O número 5 não apareceu na lista.')
print('\033[35m-=\033[m' * 30)
