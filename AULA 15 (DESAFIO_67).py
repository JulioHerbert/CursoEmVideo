num = n = 0
cont = 1
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num <= -1:
        break
    for n in range(1, 11):
        print(f'{num} x {n} = {num*n}')
print('PROGRAMA ENCERRADO!')
        

    
