a = int(input('Valor de A: '))
if a!=0:
    b = int(input('Valor de B: '))
    c = int(input('Valor de C: '))
    d = ((b ** 2) - (4 * a * c))
    if d == 0:
        print('Valor de delta = 0, a função possui apenas uma raíz real')
        r = d ** (1 / 2)
        raiz1 = (-b + r) / (2 * a)
        print('Raíz 1: {}'.format(raiz1))
    elif d < 0:
        print('Valor de delta < 0, a função não possui raízes reais')
    else:
        print('A função possui as raízes: ')
        r = d ** (1 / 2)
        raiz1 = (-b + r) / (2 * a)
        print('Raíz 1: {}'.format(raiz1))
        raiz2 = (-b - r) / (2 * a)
        print('Raíz 2: {}'.format(raiz2))
else:
    print('A função com A = 0 não é do segundo grau')
print('FIM')

