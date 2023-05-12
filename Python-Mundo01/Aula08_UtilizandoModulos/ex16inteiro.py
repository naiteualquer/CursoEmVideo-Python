#leia um número real qualquer e mostre na tela a porção inteira
#ex. 6.127 vira 6

import math

num = float(input('Digite um número real qualquer: '))
inteiro = math.trunc(num)

print('o número inteiro de {} é {}' .format(num, inteiro))