times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
cont = 1
print('-='*30)
for brasileirão in times:
    print('{:2}.{:2}'.format(cont,brasileirão))
    cont = cont + 1
print('-='*30)
print('Os [5] primeiros colocados: {}'.format (times[0:5]))
print('-='*30)
print('Os últimos [4] colocados: {}'.format(times[-4:20]))
print('-='*30)
print('Times em ordem alfabética: {}'.format(sorted(times)))
print('-='*30)
print('O posição do time da Chapecoense: {}'.format(times.index('Chapecoense')+1))
print('-='*30)
