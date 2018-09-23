preco = float(input('Informe o preço de um produto: '))
juros = preco * (5/100)
print('O valor do produto é {} Reais e com 5% de desconto será {} Reais'
      .format(preco, (preco-juros)))