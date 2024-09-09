n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f'Programa encerrado!\nSOMA: {soma}\nNúmeros digitados: {cont}')
