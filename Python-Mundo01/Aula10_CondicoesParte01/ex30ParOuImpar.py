#Par ou Ímpar - OK
#Leia um número inteiro
#Diga se é par ou ímpar

print('=+=' * 6)
print('  Par ou Ímpar')
print('=+=' * 6)

num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('{} é um número par' .format(num))
else:
    print('{} é um número ímpar' .format(num))