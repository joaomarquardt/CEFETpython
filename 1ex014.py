from math import trunc
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
print(f'Sua média será {trunc((n1 + n2) / 2)}')
#ou
print(f'Sua média será {(n1 + n2) //2}')
