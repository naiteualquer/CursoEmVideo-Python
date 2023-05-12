#Analisando Triângulos - OK
#Leia o comprimento de três retas
#Diga se podem ou não formar triângulo

print('Um triângulo pode ser formado se \nA < B + C \nB < A + C \nC < B + A \n')
ladoA = float(input('Qual o lado A do triângulo: '))
ladoB = float(input('Qual o lado B do triângulo: '))
ladoC = float(input('Qual o lado C do triângulo: '))

if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoB + ladoA):
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')


