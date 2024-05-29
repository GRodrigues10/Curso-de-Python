from ex108 import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de R${moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}.')
print(f'O aumento de 10% de R${moeda.moeda(p)} é R${moeda.moeda(moeda.aumentar(p))}.')
