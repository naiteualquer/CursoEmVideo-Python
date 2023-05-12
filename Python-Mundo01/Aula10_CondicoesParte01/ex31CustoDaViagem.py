#Custo da Viagem
#Pergunte a distância da viagem em km
#Calcule o preço da passagem
#0,50 por km até 200 km
#0,45 para viagens mais longas

viagem = float(input('Qual a distância da viagem: '))
atéDuzentos = 0.50
maisDuzentos = 0.45

if viagem <= 200:
    print("Sua viagem durou {} km e custará R$ {:.2f} por km" .format(viagem, atéDuzentos))
    print('Total da viagem: {}' .format(viagem * atéDuzentos))
if viagem > 200:
    print('Sua viagem durou {} km e custará R$ {:.2f} por km' .format(viagem, maisDuzentos))
    print('Total da viagem: R$ {:.2f}' .format(viagem * maisDuzentos))

print('=========FIM=========')
