# LISTA:
# Lista é uma coleção ordenada mutável. Permite membros duplicados.
lista = ['carro', 'bicicleta', 'avião', 3, 4.5, True]
print('\033[1;97mLISTA:\033[m')
for palavra in lista:
    print(palavra)
print('\n')

print('\033[1;97mTUPLA:\033[m')
# TUPLA:
# Tupla é uma coleção ordenada imutável. Permite membros duplicados.
tupla = ('Carro', 'Bicicleta', 'avião', 3, 4.5, True)
for p in tupla:
    print(p)


# DICIONÁRIO:
# Dicionário é uma coleção ordenada mutável. Não permite membros duplicados.
dicionario = {'Nome': 'carro', 'Lógica': True, 'Número': 4}
print(dicionario)

# CONJUNTOS:
# Conjuntos é uma coleção não ordenada e não indexada mutável. Não permite membros duplicados.
conjuntos = {'carro', True, 2, 3.5}
print(conjuntos)



