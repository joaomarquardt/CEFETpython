#20) Faça um programa  que leia 3 números e diga se eles podem ou não tomar um triângulo.
# Obs.: para formar um triângulo é necessário que a soma de dois lados seja sempre maior que o terceiro lado.
l1 = float(input('Digite o 1° lado do triângulo: '))
l2 = float(input('Digite o 2° lado do triângulo: '))
l3 = float(input('Digite o 3° lado do triângulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possível formar um triâgulo com esses valores.')
else:
    print('Não é possível formar um triângulo com esses valores.')
    