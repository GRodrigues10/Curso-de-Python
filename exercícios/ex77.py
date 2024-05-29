cont = 0
lista = ('Gabriel', 'Aprender', 'Programar')
for item in lista:
    print(f'\nNa palavra {item.upper()} temos ', end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
