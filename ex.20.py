n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1 + n2 + n3)/3
print('\033[1mMédia: {:.2f}'.format(media))
if media >= 7 and media < 10:
    print('\033[32mAprovado')
elif media < 7:
    print('\033[31mReprovado')
elif media == 10:
    print('\033[1;32m Aprovado com distinção')
