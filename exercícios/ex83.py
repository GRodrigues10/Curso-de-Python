expr = str(input('Digite uma expressão:'))
pilha = []
for c in expr:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão está correta!')
else:
    print('A sua expressão está errada!')

