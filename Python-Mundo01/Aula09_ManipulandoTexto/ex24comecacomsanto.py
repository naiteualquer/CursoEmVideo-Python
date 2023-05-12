#Verificando as primeiras letras de um texto - OK
#leia o nome da cidade e diga se começa com 'santo'

cid = str(input('Em que cidade você nasceu: ')).strip()

print(cid[:5].upper() == 'SANTO')
