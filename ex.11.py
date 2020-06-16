salario = float(input('Digite seu salário: '))
if salario <= 280:
    novo_salario = (salario*1.2)
    aumento = 20
    diferenca = novo_salario-salario
elif 280 < salario < 700:
    novo_salario = (salario*1.15)
    aumento = 15
    diferenca = novo_salario-salario
elif 700 < salario < 1500:
    novo_salario = (salario*1.1)
    aumento = 10
    diferenca = novo_salario-salario
else:
    novo_salario = (salario*1.05)
    aumento = 5
    diferenca = novo_salario-salario
print('Seu salário antes do reajuste era de: R$ {:.2f}'.format(salario))
print('O percentual de aumento aplicado foi de: {}%'.format(aumento))
print('O aumento foi de R$ {:.2f}'.format(diferenca))
print('Seu novo salário é de R$ {:.2f}'.format(novo_salario))
