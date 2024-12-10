sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Infome sexo válido: [M/F]!')).strip().upper()[0]
print('Seu sexo foi: {} correto?'.format(sexo))
