#leia os catetos oposto e adjacente e mostre a hipotenusa
#tem que ser triângulo retângulo

import math

ladoa = float(input('Qual o tamanho do lado a: '))
ladob = float(input('Qual o tamanho do lado b: '))

hipotenusa = float(math.hypot(ladoa,ladob))

print('A hipotenusa de {:.2f} e {:.2f} é igual a {:.2f}' .format(ladoa, ladob, hipotenusa))