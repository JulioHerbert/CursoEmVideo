from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    nasc = int(input('Digite ano de nascimento da primeira {}º pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('No total tivemos {} pessoas maiores de idade!'.format(totalmaior))
print('E no total tivemos {} pessoas menores de idade!'.format(totalmenor))
