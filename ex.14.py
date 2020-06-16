nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
if 9 <= media <=10:
    print('Média de aproveitamento: A')
    aprovado = True
elif 7.5 <= media < 9:
    print('Média de aproveitamento: B')
    aprovado = True
elif 6 <= media < 7.5:
    print('Média de aproveitamento: C')
    aprovado = True
elif 4 <= media < 6:
    print('Media de aproveitamento: D')
    aprovado = False
elif 0 <=media < 4:
    print('Média de aproveitamento: E')
    aprovado = False
print('Sua média foi {}'.format(media))

if aprovado == True:
    print('Parabéns, você foi APROVADO!')
else:
    print('Lamentamos, mas foi você foi REPROVADO!')