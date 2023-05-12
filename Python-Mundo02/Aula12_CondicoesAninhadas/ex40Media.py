#Aquele clássico da Média - OK
# Leia duas notas e faça média
# Reprovado abaixo de 5, recuperação entre 5 e 6,9 e aprovado com 7 ou mais

nota01 = float(input('Qual a primeira nota: '))
nota02 = float(input('Qual a segunda nota: '))

media = (nota01 + nota02) / 2

if media < 5:
    resultado = 'Reprovado'
elif media >= 5 and media <= 6.9:
    resultado = 'Em recuperação'
else:
    resultado = 'Aprovado'

print('Sua média foi {} e você está {}.' .format(media, resultado))