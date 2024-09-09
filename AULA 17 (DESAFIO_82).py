valores = []
pares = []
impares = []
while True:
    n1 = int(input('Digite um valor: '))
    if n1 not in valores:
        valores.append(n1)
    conti = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if conti in 'Nn':
        break
print(f'LISTA: {valores}')
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Valores pares: {pares}')
print(f'Valores impares: {impares}')
