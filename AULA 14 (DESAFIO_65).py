respot = 'Ss'
soma = média = cont = 0
maior = menor = 0
while respot in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    cont = cont + 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num        
    respot = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
média = soma / cont
print('FIM!\nTotal de números digitados: {}\nSoma entre os números: {}\nMédia entre os números: {:.2f}'.format(cont,soma,média))
print('Maior valor: {}\nMenor valor: {}'.format(maior,menor))
