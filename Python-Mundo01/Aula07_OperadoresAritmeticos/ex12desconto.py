#leia o preço do produto e mostre seu novo preço com desconto de 5%

preco = float(input('Qual o preço do produto: R$ '))
desconto = float(0.95)

print('O preço do produto com desconto de {:.2f} % ficou em R$ {:.2f}' .format(1 - desconto, preco * desconto))
