def retorna_potencia(a, b):
    potencia = pow(a, b)
    print(potencia)
    return potencia


numero = int(input('Digite um número:'))
exp = int(input('Digite um expoente:'))
retorna_potencia(numero, exp)
