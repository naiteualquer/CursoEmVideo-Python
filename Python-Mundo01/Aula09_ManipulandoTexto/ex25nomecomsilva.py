#Procurando uma string dentro de outra - OK
#leia o nome da pessoa e diga se no nome completo tem 'silva'

nome = str(input('Qual seu nome completo: ')).strip()

print('Seu nome tem Silva: {}' .format('SILVA'in nome.upper()))