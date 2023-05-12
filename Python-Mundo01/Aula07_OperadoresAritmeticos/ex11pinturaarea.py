# leia a largura e a altura de uma parede em metros, calcule a área e a quantidade necessária de tinta para pintá-la
# 1 l de tinta = pinta 2 m2

alt = int(input('Qual a altura da parede: '))
lar = int(input('Qual a largura da parede: '))
area = alt * lar
rend = area / 2

print('a área é de {} metros quadrados, como 1 litro de tinta rende 2 metros quadrados, você usará {} litros' .format(area, rend))