#Radar Eletrônico - OK
#Leia a velocidade de um carro
#Leva multa se ultrapassar 80 km/h
#Multa custa R$7,00 a cada km excedido

radar = float(input('Qual a velocidade do veículo? '))
print('Sua velocidade é de {} km/h' .format(radar))
if radar > float('80.00'):
    print('Limite de velocidade ultrapassado.')
    (print('Sua multa é de R$ {:.2f}' .format(radar*7)))
else:
    print('Tudo certo, pode prosseguir')