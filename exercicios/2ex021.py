#21) Faça um programa que leia 3 números e diga se eles podem ou não formar um triângulo,
# caso afirmativo, diga se o  triângulo é equilátero isósceles ou escaleno.
l1 = float(input('Digite o 1° lado do triângulo: '))
l2 = float(input('Digite o 2° lado do triângulo: '))
l3 = float(input('Digite o 3° lado do triângulo: '))
triangulo = ''
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        triangulo = 'EQUILÁTERO'
    if l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1 or l1 == l3 and l1 != l2:
        triangulo = 'RETÂNGULO'
    if l1 != l2 != l3:
        triangulo = 'ISÓSCELES'
    print(f'É possível formar um triângulo {triangulo} com esses lados.')
else:
    print('Não é possível formar um triângulo com esses lados.')