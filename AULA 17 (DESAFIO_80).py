lista = []
cont = 1
for c in range(0, 5):
    n = int(input(f'Digite {cont}º valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
    cont = cont + 1
print(f'Os valores digitados em ordem foram: {lista}')
