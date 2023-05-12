#quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#1 dolar = R$ 3,27

carteira = float(input('Quanto dinheiro você tem: '))
dolarCot = float(3.00)

print('com o dólar cotado a R$ {:.2f}, você pode comprar US$ {:.2f}' .format(dolarCot, carteira / dolarCot))
