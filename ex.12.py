hora = int(input('Horas trabalhadas/mês: '))
salario_hora = float(input('Salário/hora trabalhada: R$ '))
salario_bruto = salario_hora*hora
inss = salario_bruto*0.1
sindicato = salario_bruto*0.03
fgts = salario_bruto*0.11
if salario_bruto < 900:
    percentagem = 0
    ir = 0
elif 900 < salario_bruto < 1500:
    percentagem = 5
    ir = salario_bruto*0.05
elif 1500 < salario_bruto < 2500:
    percentagem = 10
    ir = salario_bruto*0.1
else:
    percentagem = 20
    ir = salario_bruto*0.20
descontos = ir + inss
salario_liquido = salario_bruto-descontos
print('*'*30)
print('Salário Bruto     :   ({} x {})   R$ {:.2f}'.format(salario_hora, hora, salario_bruto))
print('(-) IR ({}%)       :               R$ {:.2f}'.format(percentagem, ir))
print('(-) INSS (10%)    :               R$ {:.2f}'.format(inss))
print('FGTS (11%)        :               R$ {:.2f}'.format(fgts))
print('Total de descontos:               R$ {:.2f}'.format(descontos))
print('Salário Líquido   :               R$ {:.2f}'.format(salario_liquido))
