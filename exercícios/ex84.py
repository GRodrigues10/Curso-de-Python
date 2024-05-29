pessoas = list()
dados = list()
cont = 0
maior = 0
menor = float('inf')
p_leve = ''
p_gorda = ''
while True:
    dados.append(str(input('Digite o seu nome:')))
    dados.append(float(input('Digite o seu peso:')))
    pessoas.append(dados[:])
    dados.clear()
    cont = cont + 1
    op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while op not in 'SN':
        print('Opção Inválida!')
        op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break

for pessoa in pessoas:
    nome = pessoa[0]
    peso = pessoa[1]
    if peso > maior:
        maior = peso
        p_gorda = nome

    if peso < menor:
        menor = peso
        p_leve = nome
print(f'Foram Cadastradas {cont} pessoas.')
print(f'A pessoa mais gorda é {p_gorda}')
print(f'A pessoa mais leve é {p_leve}')
print('Fim do programa!')




