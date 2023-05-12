#Aumentos Múltiplos - OK
#Leia um salário e calcule o aumento
#Acima de 1.250, aumenta 10%
#Abaixo de 1.250, aumenta 15%

salario = float(input('Qual o salário atual: '))

acima = 1.10
abaixo = 1.15

if salario > 1250:
    print('Seu reajuste será de {:.2f}%, ficando o novo valor em R$ {:.2f}' .format((acima - 1) * 100, salario * acima))
else:
    print('Seu reajuste será de {:.2f}%, ficando o novo valor em R$ {:.2f}' .format((abaixo -1 ) * 100, salario * abaixo))
