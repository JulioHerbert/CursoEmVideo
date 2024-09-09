termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print('{} '.format(c), end=' > ')
print('ACABOU!')
