dias = float(input('Por quantos dia você alugou o Carro: '))
km = float(input('Quandos Km você andou: '))
carro = dias * 60
kmRodado = km * 0.15
total = float(carro + kmRodado)
print('O preço total a ser pagado é de R${}'.format(total))