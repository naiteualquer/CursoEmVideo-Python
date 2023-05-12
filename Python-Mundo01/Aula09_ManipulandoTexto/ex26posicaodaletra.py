#Primeira e última ocorrência de uma string
#leia uma frase e mostre
#quanto vezes 'a'
#primeira posição do 'a'
#última posição do 'a'

frase = str(input('Digite qualquer frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase' .format(frase.count('A')))
print('A primeira posição da letra A é de número {}' .format(frase.find('A')+1))
print('A última posição da letra A é de número {}' .format(frase.rfind('A')+1))

