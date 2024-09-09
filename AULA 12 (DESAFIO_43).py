peso = float(input('Digite seu peso: (Kg)'))
altura = float(input('Digite sua altura: '))
imc = peso /(altura * altura)
print('Peso: {}\nAltura: {}\nIMC: {:.1f}'.format(peso,altura,imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA!')


