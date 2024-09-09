n1 = [[], []]
valor = 0
cont = 1
for c in range(1, 8):
    valor = int(input(f'Digite {cont}º valor: '))
    cont = cont + 1
    if valor % 2 == 0:
        n1[0].append(valor)
    else:
        n1[1].append(valor)
n1[0].sort()
n1[1].sort()
print(f'Valores pares: {n1[0]}')
print(f'Valores ímpares: {n1[1]}')
