print('Responda as questões abaixo com S = SIM ou N = NÃO: ')

p1 = str(input('Telefonou para a vítima? ')).upper()
s = n = 0
while p1 not in 'SN':
    print('Opção inválida')
    p1 = str(input('Telefonou para a vítima? ')).upper()
if p1 == 'S':
    s += 1

p2 = str(input('Esteve no local do crime? ')).upper()
while p2 not in 'SN':
    print('Opção inválida')
    p2 = str(input('Esteve no local do crime? ')).upper()
if p2 == 'S':
    s += 1

p3 = str(input('Mora perto da vítima? ')).upper()
while p3 not in 'SN':
    print('Opção inválida')
    p3 = str(input('Mora perto da vítima? ')).upper()
if p3 == 'S':
    s += 1

p4 = str(input('Devia para a vítima? ')).upper()
while p4 not in 'SN':
    print('Opção inválida')
    p4 = str(input('Devia para a vítima? ')).upper()
if p4 == 'S':
    s += 1

p5 = str(input('Já trabalhou com a vítima? ')).upper()
while p5 not in 'SN':
    print('Opção inválida')
    p5 = str(input('Já trabalhou com a vítima? ')).upper()
if p5 == 'S':
    s += 1

print('Você respondeu a {} perguntas com SIM e foi classificado como '.format(s), end='')

if 0 < s <= 2:
    print('SUSPEITO')
elif 3 <= s <= 4:
    print('CUMPLICE')
elif s == 5:
    print('ASSASSINO')
else:
    print('INOCENTE')