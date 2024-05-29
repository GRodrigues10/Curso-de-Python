n = int(input('Digite um número:'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
        print('\033[34m', end='')
    else:
        print('\033[97m', end='')
    print(f'{c}', end='')
if tot == 2:
    print('\n\033[mÉ primo')
else:
    print('\n\033[mNão é primo')