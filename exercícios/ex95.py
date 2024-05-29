jogadores = list()
while True:
    jogador = dict()
    soma = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []

    for p in range(1, jogador['partidas'] + 1):
        gols = int(input(f'  => Quantos gols {jogador["nome"]} fez na {p}° partida? '))
        jogador['gols'].append(gols)
        soma += gols
    jogador['total'] = soma
    jogadores.append(jogador)

    op = str(input('Deseja Continuar? [S/N]:')).strip().upper()[0]
    while op not in 'SN':
        print('Opção Inválida!')
        op = str(input('Deseja Continuar? [S/N]:')).strip().upper()[0]
    if op == 'N':
        break
cont = 1
# Inicialize o contador fora do loop
print("Partida | Nome                 | Gols por Partida                      | Total de Gols")
for cont, jogador in enumerate(jogadores, start=1):
    gols_por_partida = ' '.join(str(g) for g in jogador["gols"])  # Transforma os gols em uma string separada por espaços
    print(f'{cont: <7} | {jogador["nome"]: <20} | {gols_por_partida: <35} | {jogador["total"]: <13}')

opc = int(input('Deseja ver os dados de qual jogador? (999 para interromper): '))
while opc != 999:
    if opc >= 1 and opc <= len(jogadores):
        jogador = jogadores[opc - 1]  # Jogadores são indexados de 0 em diante, mas opc começa em 1
        print("Dados do jogador:")
        for k, v in jogador.items():
            print(f'{k}: {v}')
    else:
        print("Jogador não encontrado.")

    opc = int(input('Deseja ver os dados de qual jogador? (999 para interromper): '))







