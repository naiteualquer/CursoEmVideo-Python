#converta uma temperatura digitada em C para F

celsius = float(input('Qual a temperatura em Celsius:'))
convertido = ((9*celsius)/5)+32

print('A temperatura de {}°C é {}°F' .format(celsius, convertido))