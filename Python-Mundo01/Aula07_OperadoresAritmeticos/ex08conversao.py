#programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

tamanho = int(input('qual tamanho em metros deseja converter: '))
convCm = int(tamanho * 100)
convMm = int(tamanho * 1000)

print('metro para cm: {} cm \nmetro para milímetro: {} mm' .format(convCm, convMm))

