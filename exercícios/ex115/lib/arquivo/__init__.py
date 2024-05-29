from ex115.lib.interface import *


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+') # 'wt' escreva um arquivo. '+' se o arquivo não existir... crie!
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        with open(nome, 'rt') as arquivo:
            cabeçalho('Pessoas cadastradas!')
            for linha in arquivo:
                dado = linha.split(';')
                if len(dado) >= 2:
                    nome = dado[0].strip()  # Remove espaços em branco extras ao redor do nome
                    idade = dado[1].replace('\n', '')  # Remove o caractere de nova linha
                    print(f'{nome:<30} {idade} anos')  # Ajusta o espaçamento entre nome e idade
                else:
                    print(f'Linha inválida: {linha}')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        with open(arq, 'at') as a:
            a.write(f'{nome};{idade}\n')  # Salva os dados no formato nome;idade\n
        print(f'Novo registro de {nome} adicionado!')
    except Exception as e:
        print(f'Houve um erro ao adicionar o registro: {e}')






