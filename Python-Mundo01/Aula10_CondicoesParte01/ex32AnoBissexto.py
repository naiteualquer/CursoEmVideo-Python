#Ano Bissexto - OK
#Leia um ano e diga se é bissexto

ano = int(input('Digite um ano para saber se ele é bissexto: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto' .format(ano))
else:
    print('O ano de {} não é bissexto.' .format(ano))
