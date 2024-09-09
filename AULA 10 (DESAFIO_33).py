num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro númeor: '))
#CALCULO DE MENOR:
if num1<num2 and num1<num3:
    menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num2 and num3<num1:
    menor = num3
#CALCULO DE MAIOR:
if num1>num3 and num1>num2:
    maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num2 and num3>num1:
    maior = num3
print('Menor número foi: {}'.format(menor))
print('Maior número foi: {}'.format(maior))
else:
    letra.isalpha(num1,num2,num3):
        print('Por favor digite um número!')


