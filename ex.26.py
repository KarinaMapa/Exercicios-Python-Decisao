litros = float(input('Quantos litros deseja colocar? '))
combustivel = str(input('Qual tipo de combustível? [A] - Álcool ou [G] - Gasolina ')).upper()
while combustivel not in 'AG':
    print('Opção inválida')
    combustivel = str(input('Qual tipo de combustível? [A] - Álcool ou [G] - Gasolina ')).upper()
alcool = 1.90
gasolina = 2.50
valor = 0
if litros < 20:
    if combustivel == 'A':
        valor = (alcool*litros)*0.97
    else:
        valor = (gasolina*litros)*0.96
else:
    if combustivel == 'A':
        valor = (alcool*litros)*0.95
    else:
        valor = (gasolina*litros)*0.94
print('O valor total a pagar é de R$ {:.2f}'.format(valor))