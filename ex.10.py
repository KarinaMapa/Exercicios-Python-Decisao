turno = str(input('Em que turno você estuda? [M - MATUTINO, V - VESPERTINO, N - NOTURNO] ')).upper()
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido!')