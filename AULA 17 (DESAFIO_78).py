num = []
cont = 1
menor = 0
maior = 0
for c in range(0, 5):
    num.append(int(input(f'Digite o {cont}º valor para a posição {c}: ')))
    cont = cont + 1
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
for i, v in enumerate(num):
    if v == maior:
        print(f'Maior valor: {maior} encontrado na posição: {i}')
for i, v in enumerate(num):
    if v == menor:
        print(f'Menor valor: {menor} encontrado na posição: {i}')
        
