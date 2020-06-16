n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A média do aluno foi {:.1f}'.format(media))

if media >= 7 and media != 10:
    print('APROVADO!')
elif media == 10:
    print('APROVADO COM DISTINÇÃO!')
else:
    print('REPROVADO')