n = cont = soma = 0
while True:
    n = int(input('Digite um número ou [999] para parar: '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f'PROGRAMA ENCERRADO!\nTOTAL DE NÚMEROS DIGITADOS: {cont}\nSOMA: {soma}')
