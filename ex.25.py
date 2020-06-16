n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print('''Selecione uma opção: 
      [1] - SOMA
      [2] - SUBTRAÇÃO
      [3] - MULTIPLICAÇÃO
      [4] - DIVISÃO''')
opcao = int(input('Opção: '))
while opcao > 4 or opcao < 1:
    print('Opção inválida!')
    opcao = int(input('Opção: '))
if opcao == 1:
    result = n1 + n2
elif opcao == 2:
    result = n1 - n2
elif opcao == 3:
    result = n1 * n2
elif opcao == 4:
    result = n1 / n2
print('^'*40)
print('O resultado da operação é {}'. format(result))
print('{} é '.format(result), end=' ')
if result % 2 == 0:
    print('par', end=', ')
else:
    print('ímpar', end=', ')
if result >= 0:
    print('positivo', end= ' e')
else:
    print('negativo', end=' e')
if result % 1 != 0:
    print(' decimal')
else:
    print(' inteiro')