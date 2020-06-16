l1 = int(input('Medida lado 1: '))
l2 = int(input('Medida lado 2: '))
l3 = int(input('Medida lado 3: '))
#Verifica se forma um triângulo
if l1 < (l2+l3) and l1 > abs(l2-l3) or l2 < (l1+l3) and l2 > abs(l1-l3) or l3 <(l1+l2) and l3 > abs(l1-l2):
    print('Com os lados indicados temos um TRIÂNGULO', end=' ')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Com os lados indicados não temos um triângulo')

