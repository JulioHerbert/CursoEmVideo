while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 21:
        num = int(input('Tente novamente. Digite um número entre 0 e 20'))
    print('Você digitou o número: {}'.format(num))
    break
print('FIM')
    
        
