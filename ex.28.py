print('''Qual tipo de carne você deseja?
[1] - Filé Duplo
[2] - Alcatra    
[3] - Picanha
''')
opcao = int(input('Opção: '))

quilos = float(input('Quantos quilos você deseja? '))
if opcao == 1:
    carne = 'Filé Duplo'
    if quilos <= 5:
        preco = 4.90
    else:
        preco = 5.80
elif opcao == 2:
    carne = 'Alcatra'
    if quilos <= 5:
        preco = 5.90
    else:
        preco = 6.80
elif opcao == 3:
    carne = 'Picanha'
    if quilos <= 5:
        preco = 6.90
    else:
        preco = 7.80
valor_total = quilos*preco
pagamento = str(input('Deseja pagar com cartão Tabajara? [S/N]')).upper()
while pagamento not in 'SN':
    print('Opção inválida')
    pagamento = str(input('Deseja pagar com cartão Tabajara? [S/N]')).upper()
if pagamento == 'S':
    modo = 'Cartão tabajara'
    desconto = (valor_total*0.05)
else:
    modo = 'Outra modalidade'
    desconto = valor_total*0
valor_desc = valor_total - desconto
print('~'*40)
print('       CUPOM FISCAL  ')
print('~'*40)
print('TIPO   QUANTIDADE   PREÇO TOTAL     PAGAMENTO     DESCONTO   VALOR A PAGAR')
print('{}    {}      R$ {:.2f}    {}    R${:.2f}     R${:.2f}'.format(carne, quilos, valor_total, modo, desconto, valor_desc))