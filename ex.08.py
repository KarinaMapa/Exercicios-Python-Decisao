p1 = float(input('Digite o preço do produto 1: R$  '))
p2 = float(input('Digite o preço do produto 2: R$  '))
p3 = float(input('Digite o preço do produto 3: R$  '))
menor = 0
if p1==p2==p3:
    print('Escolha qualquer produto, os três tem o mesmo valor.')
elif p1<p2 and p1<p3:
    menor = p1
elif p2<p3:
    menor = p2
else:
    menor = p3
print('O produto mais barato custa R$ {:.2f}, você deveria comprar ele.'.format(menor))