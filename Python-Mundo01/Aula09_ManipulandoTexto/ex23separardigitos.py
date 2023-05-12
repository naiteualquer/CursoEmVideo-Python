# Separando dígitos de um número = OK
#leia de 0 a 9999 qualquer e mostre os dígitos separados
#ex: 153
# 1
# 5
# 3

numero = int(input('Digite um número entre 0 e 9999: '))

#sem usar if else
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10


print('unidade: {}' .format(u))
print('dezena: {}' .format(d))
print('centena: {}' .format(c))
print('milhar: {}' .format(m))



