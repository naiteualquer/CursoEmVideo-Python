# Comparando Números - OK
# Leis dois números inteiros
# Mostre se o primeiro ou segundo é maior ou então se eles são iguais

numA = int(input('Digite um número: '))
numB = int(input('Digite um número: '))

if numA > numB:
    maior = 'o número {} é maior' .format(numA)
elif numB > numA:
    maior = 'o número {} é maior' .format(numB)
else:
    maior = 'os números {} e {} são iguais.' .format(numA, numB)

print(maior)
