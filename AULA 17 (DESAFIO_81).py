valores = []
conti = ''
while True:
    n1 = int(input('Digite um valor: '))
    if n1 not in valores:
        valores.append(n1)
    conti = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if conti in 'Nn':
        break
print(f'Lista: {valores}')
print(f'Foram digitados: {len(valores)} números.')
valores.sort(reverse=True)
print(f'Valores da lista de forma decrescente: {valores}')
if 5 in valores:
    print(f'Valor 5 foi digitado.')
else:
    print(f'Valor 5 não foi encontrado.')
