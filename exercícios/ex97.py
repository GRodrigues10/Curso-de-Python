def escreva(msg):
    tam = len(msg) + 4 # Esse comando deixa a mensagem centralizada. O '+ 4' é para colocar bordas. duas para um lado e duas para o outro.
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal:
escreva('Gabriel Rodrigues')
escreva('Duke')
escreva('Jar Jar Binks')
