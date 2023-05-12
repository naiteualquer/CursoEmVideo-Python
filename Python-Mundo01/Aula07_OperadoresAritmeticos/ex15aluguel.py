#pergunta a quantidade de km rodados e de dias de um carro alugado

dias = int(input('O aluguel foi de quantos dias: '))
km = int(input('O percurso foi de quantos km: '))

diaria = 60
kmRodado = float(0.15)

print('Você alugou por {} dias e {} km. A diária custa R$ {} e adicional de R$ {} por km rodado.' .format(dias,km,diaria,kmRodado))
print('O preço final do aluguel foi de R$ {:.2f}, sendo R$ {:.2f} de diária e R$ {} de km rodado' .format(dias*diaria+km*kmRodado,dias*diaria, km*kmRodado))
