n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
maior = 0
if n1 > n2:
    maior = n1
else:
    maior = n2
print('O maior valor entre {} e {} foi {}'.format(n1, n2, maior))