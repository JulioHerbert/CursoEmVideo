num = 0
cont = 0
soma = 0
num = int(input('Digite um número para continuar ou [999] para parar: '))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um número para continuar ou [999] para parar: '))
print('FIM!\nTotal de números digitados: {}\nSoma entre os números digitados: {}'.format(cont,soma))
