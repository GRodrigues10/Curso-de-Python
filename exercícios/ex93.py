jogador = dict()
soma = 0

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []

for p in range(1, jogador['partidas'] + 1):
    gols = int(input(f'Quantos gols {jogador["nome"]} fez na {p}° partida? '))
    jogador['gols'].append(gols)
    soma += gols

jogador['total'] = soma

print('\n')
print('\033[1;97m-=\033[m' * 35)
print(jogador)
print('\033[1;97m-=\033[m' * 35)
print('\n')
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('\n')
print('\033[1;97m-=\033[m' * 35)

print(f'O jogador {jogador["nome"]} tem {jogador["partidas"]} partidas')
for p in range(1, jogador['partidas'] + 1):
    print(f'    => Na partida {p}, o jogador {jogador["nome"]} fez {jogador["gols"][p-1]} gols.')

print(f'O jogador {jogador["nome"]} tem um total de {jogador["total"]} gols em {jogador["partidas"]} partidas.')

