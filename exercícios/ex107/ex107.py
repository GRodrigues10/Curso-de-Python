import moeda

numero = float(input('Digite o preço:R$'))
print(f'A metade de R${numero} é R${moeda.metade(numero):.2f}.')
print(f'O dobro de R${numero} é R${moeda.dobro(numero):.2f}.')
print(f'O aumento de 10% de R${numero} é R${moeda.aumentar(numero):.2f}.')
