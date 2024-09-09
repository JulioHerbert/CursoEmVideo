n1 = str(input('Digite o nome completo: '))
up = n1.upper().strip()
print('Nome completo maiúsculo: {}'.format(up))
low = n1.lower().strip()
print('Nome completo minúsculo: {}'.format(low))
cont = len(low) - n1.count(' ')
print('Seu nome ao todo tem: {} caracteres!'.format(cont))

div = low.split()

count2 = len(div[0])

print('Seu primeiro nome tem: {}'.format(count2))





