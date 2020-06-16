n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
maior = 0
if n1>n2 and n1>n3:
    maior = n1
elif n2>n1 and n2>n3:
    maior = n2
else:
    maior = n3
print('O maior número digitado foi %s'%(maior))
menor = 0
if n1<n2 and n1<n3:
    menor = n1
elif n2<n1 and n2<n3:
    menor = n2
elif n1==n2==n3:
    print('Os números são iguais')
else:
    menor = n3
print('O menor número digitado foi %s'%(menor))
