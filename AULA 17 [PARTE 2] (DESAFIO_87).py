matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = somal = maior = menor = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma = soma + matriz[l][c]
    print()
print(f'A soma dos elementos pares são: {soma}')
for l in range(0,3):
    somal = somal + matriz[l][2]
print(f'A soma dos valores da terceira coluna são: {somal}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
        menor = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
        if matriz[1][c] < menor:
            menor = matriz[1][c]
print(f'O maior valor da segunda linha foi: {maior}')
print(f'E o menor valor da segunda linha foi: {menor}')    

    
