#maior, igual e menor a mil
maior = 0
igual = 0
menor = 0
n = 1
while n != 101:
    num = int(input(f'Digite o {n}° número: '))
    if num > 1000:
        maior += 1
    elif num == 1000:
        igual += 1
    elif num < 1000:
        menor += 1
print(f'MAIOR QUE MIL: {maior} números digitados'
      f'\nIGUAL A MIL: {igual} números digitados'
      f'\nMENOR QUE MIL: {menor} números digitados')
