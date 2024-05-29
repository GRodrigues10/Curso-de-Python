from ex109 import moeda

num = float(input('Digite um valor: R$'))
print(f'O valor {moeda.formatacao(num)} com 10% de aumento fica por {moeda.aumento(num, r=True)}')
print(f'O valor {moeda.formatacao(num)} com 13% de desconto fica por {moeda.diminuir(num, r=True)}')
print(f'O dobro de {moeda.formatacao(num)} é {moeda.dobro(num, r=True)}')
print(f'A metade de {moeda.formatacao(num)} é {moeda.metade(num, r=True)}')