def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols.')


n = str(input('Qual o nome do jogador? ')).strip()
g = str(input(f'Quantos gols o jogador {n} fez? ')).strip()

if g.isnumeric():
    g = int(g)
else:
    g = 0

if not n:  # Se 'n' estiver vazio
    ficha(gols=g)
else:
    ficha(n, g)
