# Tratamento de erros e exceções:
# operação
try:
    a = int(input('Numero:'))
    b = int(input('Numero:'))
    r = a / b

# falhou
#except Exception as erro:
   #print(f'O problema foi {erro.__class__}')'''

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')

# deu certo
else:

    print(r)

# certo / falha
finally:
    print('Volte sempre! Muito Obrigado!')


