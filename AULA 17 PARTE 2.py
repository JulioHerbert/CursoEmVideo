galera = list()
dados = list()
maior = menor = 0
for c in range(0, 3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade!')
        maior = maior + 1
    else:
        print(f'{p[0]} é menor de idade!')
        menor = menor + 1
print(f'No total tivemos {maior} pessoa maior de idade')
print(f'E {menor} pesso menor de idade')
    
