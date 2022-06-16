from math import hypot
lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
hipo = lado1 ** 2 + lado2 ** 2
print(f'A hipotenusa do triângulo com lados {lado1} e {lado2} será {hipo ** (1/2):.1f}')
#ou
print(f'A hipotenusa do triângulo com lados {lado1} e {lado2} será {hypot(lado1, lado2):.1f}')