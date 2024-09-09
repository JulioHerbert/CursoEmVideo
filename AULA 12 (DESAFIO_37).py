n1 = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha a forma de conversão:\n[1] para BINÁRIO\n[2] para OCTAL\n[3] para HEXADECIMAL\nESCOLHA: '))
if escolha == 1:
    print('{} em BINÁRIO: {}'.format(n1,bin(n1)[2:]))
elif escolha == 2:
    print('{} em OCTAL: {}'.format(n1,oct(n1)[2:]))
elif escolha == 3:
    print('{} em HEXADECIMAL: {}'.format(n1,hex(n1)[2:]))
else:
    print('Por favor digite um número dentro da opções...!')
    
    
