morango = float(input('Quantos kilos de morango deseja? '))
maca = float(input('Quantos kilos de maça deseja? '))
if morango <= 5:
    preco_morango = 2.5
else:
    preco_morango = 2.20
if maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50
valor_total = (morango*preco_morango) + (maca*preco_maca)
quilos = morango + maca
if quilos > 8 or valor_total > 25:
    preco_desconto = valor_total*0.90
else:
    preco_desconto = valor_total
print('Valor total da compra R$ {:.2f}'.format(preco_desconto))