from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

# O '*' é para importar tudo!

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
       ler_arquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leia_int('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema...')
        break
    else:
        print('\033[31mERRO!\033[m')
    sleep(1)


