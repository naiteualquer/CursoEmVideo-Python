#Jogo da Adivinhação 1.0 - OK
#Computador pensar num número de 0 a 5
#Usuário tenta adivinhar o número
#Programa informa que usuário acertou ou errou

import random

num = int(input('Em qual número de 0 a 5 eu estou pensando? '))
numAle = print('Estava pensando no número {}' .format(random.randint(0,5)))

if num == numAle:
    print('Parabéns, você acertou o número')
else:
    print('Errado! Boa sorte na próxima tentativa')
