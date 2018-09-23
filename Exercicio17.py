import  math
catetoA = float(input('Informe o valor do Cateto A: '))
catetoB = float(input('Informe o valor do Cateto B: '))
hip = math.sqrt((math.pow(catetoA,2)) + (math.pow(catetoB,2)))
print('O valor ta Hipotenusa é {}'.format(hip))