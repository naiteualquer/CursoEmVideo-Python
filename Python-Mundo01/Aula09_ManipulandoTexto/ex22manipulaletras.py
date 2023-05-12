#Analisador de Textos - OK
#nome da pessoa com
#tudo maiúsculo
#tudo minúsculo
#número de letras (sem contar espaços)
#quantidade de letras do primeiro nome

nome = str(input('Qual seu nome: '))

mais = nome.upper()
minus = nome.lower()
nomeSemEspaco = len(nome.replace(" ",""))
letrasPrimeiro = nome.find(" ")



print('O nome completo em letras maiúsculas é {}' .format(mais))
print('O nome completo em letras minúscula é {}' .format(minus))
print('A quantidade de letras do nome é {}' .format(nomeSemEspaco))
print('O primeiro nome tem {} letras' .format(letrasPrimeiro))