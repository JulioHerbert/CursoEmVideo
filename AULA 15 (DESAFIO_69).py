contdezoito = 0
conthomens = 0
mul = 0
while True:
    idade = int(input('Digite idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite sexo do índividuo: [M/F] ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja encerrar?: [S/N]')).strip().upper()[0]
    if idade >= 18:
        contdezoito = contdezoito + 1
    if sexo == 'M':
        conthomens = conthomens + 1
    if sexo == 'F' and idade < 20:
        mul = mul + 1
    if continuar == 'N':
        break
print(f'PROGRAMA ENCERRADO!\nTotal de pessoas acima de 18 anos: {contdezoito}')
print(f'Homens cadastrados: {conthomens}')
print(f'Mulheres que tem menos de 20: {mul}')
