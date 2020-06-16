n = int(input('Digite um número inteiro menor que 1000: '))
centena = n // 100
dezena = (n-(centena*100)) // 10
unidade = (n - (centena*100) - (dezena*10))


print('O número digitado {} tem {} centenas, {} dezenas e {} unidades.'.format(n, centena, dezena, unidade))