soma = 0
contador = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        soma = soma + count
        contador = contador + 1
    print(count, end=' ')
print('\nA soma de todos esses números resulta em: {}\nTotal de números na soma: {}'.format(soma,contador))
