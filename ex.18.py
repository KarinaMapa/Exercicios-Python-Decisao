data = (input('Digite uma data [xx/xx/xxxx]: '))
while len(data) < 10:
    print('Formato de data inválido, por favor, digite novamente:')
    data = input('Digite uma data [xx/xx/xxxx]: ')
dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])
if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 0:
    True
    print('Data válida')
else:
    False
    print('\033[31mData inválida')

print(data)

