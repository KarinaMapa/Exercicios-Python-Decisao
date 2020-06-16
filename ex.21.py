saque = int(input('Qual valor deseja sacar? '))
while saque > 600 or saque < 10:
    print('Valor não permitido, saque mínimo de 10 reais, saque máximo de 600 reais')
    saque = int(input('Qual valor deseja sacar? '))
n100 = n50 = n10 = n5 = n1 =0
from math import floor
n100 = saque // 100
floor(n100)
n50 = (saque - (n100*100)) // 50
floor(n50)
n10 = (saque - (n100*100) - (n50*50)) // 10
floor(n10)
n5 = (saque - (n100 * 100) - (n50*50) - (n10*10)) // 5
floor(n5)
n1 = (saque - (n100*100) - (n50*50) - (n10*10) - (n5*5)) // 1
print('Saque de {} notas de 100, {} notas de 50, {} notas de 10, {} notas de 5, {} notas de 1 real'.format(n100, n50, n10, n5, n1))
