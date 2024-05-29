from auxiliar import title
from auxiliar import content
jogadores = list()
title()
content()
cont = 1
maior = 0
menor = float('inf')
nome_goleador = 0
nome_bagre = 0
while True:
    armazenar = dict()
    armazenar['nome'] = str(input(f'Digite o nome do jogador {cont}:'))
    armazenar['time'] = str(input(f'Digite o time do jogador {armazenar["nome"]}:'))
    armazenar['gols'] = int(input(f'Quantos gols {armazenar["nome"]} fez pelo {armazenar["time"]}?'))
    cont += 1

    jogadores.append(armazenar)
    op = str(input('Deseja Continuar cadastrando mais jogadores? [S/N]')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Deseja Continuar cadastrando mais jogadores? [S/N]')).strip().upper()[0]
    if op == 'N':
        break
print('  NOME  |  TIME  |  GOLS')
for players in jogadores:
    nome = players['nome']
    time = players['time']
    gols = players['gols']
    if gols > maior:
        maior = gols
        nome_goleador = nome
    if gols < menor:
        menor = gols
        nome_bagre = nome

    print(f'{nome} | {time} | {gols}')
print('[1] - Jogador que fez mais gols.')
print('[2] - Jogador que fez menos gols.')
print('[3] - Sair do Programa!.')

while True:
    dados = input('Você deseja ver o que? ').strip()
    if dados not in ['1', '2', '3']:
        print('[ERRO] - Opção Inválida!')
        continue

    if dados == '1':
        print(f'O jogador que fez mais gols foi {nome_goleador}, que marcou {maior} gols.')
    elif dados == '2':
        print(f'O jogador que fez menos gols foi {nome_bagre}, que marcou {menor} gols.')
    else:
        break
    print('[1] - Jogador que fez mais gols.')
    print('[2] - Jogador que fez menos gols.')
    print('[3] - Sair do Programa!.')
    print('\n')

print('FIM DO PROGRAMA!\nVolte Sempre, PATINHO!🤪')


