#leia um ângulo e mostre seno, cosseno e tangente

import math

ang = int(input('Qual ângulo você deseja saber o seno, cosseno e tangente: '))
rad = math.radians(ang) #converte de graus para radianos

sen = float(math.sin(rad)) #calcula o seno
cos = float(math.cos(rad)) #calcula o cossenho
tg = float(math.tan(rad)) #calcula a tangente

print('o seno de {}º é {:.4f}' .format(ang,sen))
print('o cosseno de {}º é {:.4f}' .format(ang,cos))
print('a tangente de {}º é {:.4f}' .format(ang,tg))
