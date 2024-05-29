tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
         'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    n = int(input('Digite um Número:'))
    if n >=0 and n <= 20:
        break
    print('Tente novamente!', end='')
print(f'Você digitou o número {tupla[n]}.')






