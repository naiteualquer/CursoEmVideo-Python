#Primeiro e último nome de um pessoa - OK
#leia o nome completo e mostre primeiro e último separadamente

nome = str(input('Qual seu nome completo: ')).strip()
nomeDividido = nome.split()

print('Seu primeiro nome é: {}' .format(nomeDividido[0]))
print('Seu último nome é: {}' .format(nomeDividido[len(nomeDividido)-1]))