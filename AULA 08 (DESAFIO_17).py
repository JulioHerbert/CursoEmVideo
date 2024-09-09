op = float(input('Digite comprimento do cateto oposto: '))
ad = float(input('Digite comprimento do cateto adjacente: '))

cal = (op ** 2 + ad ** 2) ** (1/2)

print('Comprimento da hipotenusa: {:.2f}'.format(cal))
