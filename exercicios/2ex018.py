#18) Faça um programa que leia 5 números e identifique o maior e o menor.
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))
n5 = int(input('Digite o 5° número: '))
max = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3
if n4 > max:
    max = n4
if n5 > max:
    max = n5
print(f'O maior número digitado foi {max}')
min = n1
if n2 < min:
    min = n2
if n3 < min:
    min = n3
if n4 < min:
    min = n4
if n5 < min:
    min = n5
print(f'O menor número foi {min}')