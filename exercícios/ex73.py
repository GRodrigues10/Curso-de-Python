lista = ('Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Flamengo',
         'Atlético Mineiro', 'Atlético Paranaense', 'Fluminense',
         'São Paulo', 'Fortaleza', 'Internacional', 'Cuiabá', 'Corinthians',
         'Santos', 'Bahia', 'Vasco da Gama', 'Cruzeiro', 'Goiás', 'Coritiba',
         'América Mineiro')
print('=' * 30)
print(f'\033[1;97mLista de times do Brasileirão:\033[m\033[1;36m{lista}\033[m')
print('=' * 30)
print(f'\033[1;97mOs 6 primeiros são:\033[m\033[1;34m{lista[0:6]}\033[m')
print('=' * 30)
print(f'\033[1;97mOs 4 últimos são:\033[m\033[1;31m{lista[15:20]}\033[m')
print('=' * 30)
print(f'\033[1;97mTimes em ordem alfabética:\033[m\033[1;36m{sorted(lista)}\033[m')
print('=' * 30)
print(f'\033[1;33mO time do {lista[7]} está na posição 8.\033[m')
print('=' * 30)
