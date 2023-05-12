#Analisando Triângulo 2.0
#Refaz o ex 35 e mostra o tipo de triângulo
#equilátero (todos iguais), isósceles (dois iguais) ou escaleno (todos diferentes)

print('Um triângulo pode ser formado se \nA < B + C \nB < A + C \nC < B + A \n')
ladoA = float(input('Qual o lado A do triângulo: '))
ladoB = float(input('Qual o lado B do triângulo: '))
ladoC = float(input('Qual o lado C do triângulo: '))

if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoB + ladoA):
    print('Pode formar um triângulo')
    if ladoA > ladoB:
        print('escaleno')
    if ladoB > ladoC: # TODO: descrever as condições do triângulo
        print('equilátero')# TODO: colocar texto e referência exata
else:
    print('Não pode formar um triângulo')

