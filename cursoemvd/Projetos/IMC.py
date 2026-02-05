# Peça o peso e a altura do usuário, calcule o IMC e, usando condicionais,
# informe se o usuário está abaixo do peso, peso normal, sobrepeso ou obeso.

peso = float(input('Qual o seu peso? '))
alt = float(input('Qual a sua altura? '))
imc = peso/ alt**2
print(f'seu imc é {imc:.2f}')

if imc < 18.5:
    print('	Abaixo do peso')
elif imc < 24.9 :
    print('Peso normal')
elif imc < 29.9:
    print('Sobrepeso')
elif imc <  34.9:
    print('	Obesidade Grau I')
elif imc <  39.9:
    print('	Obesidade Grau II')
elif imc < 40.0:
    print('	Obesidade Grau III')
else:
    print('sem resposas')