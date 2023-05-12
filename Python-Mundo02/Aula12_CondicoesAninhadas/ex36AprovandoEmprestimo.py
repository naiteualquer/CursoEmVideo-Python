# AProvando Empréstimo - OK
# TODO:Perguntar qual o valor da casa, salário do comprador e em quantos anos vai pagar
# TODO:Calcular prestação mensal menor que 30% do salário ou nega o empréstimo

valor = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário mensal: '))
anos = int(input('Quer pagar em quantos anos: '))

valorMensal = (valor // (anos * 12))

if valorMensal >= float(salario * 0.30):
    print('O valor da prestação de R$ {:.2f} ultrapassa 30% da sua renda mensal.' .format(valorMensal))
else:
    print('Seu financiamento foi concedido. Você pagará R$ {:.2f} mensalmente.' .format(valorMensal))
