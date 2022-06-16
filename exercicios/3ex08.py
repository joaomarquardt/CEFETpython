impar = 0
n = 1
while n != 101:
    num = int(input(f'Digite o {n}° número: '))
    if num % 2 == 1:
        impar += 1
    n += 1
if impar == 0:
    print('Não foi digitado nenhum número ímpar')
elif impar == 1:
    print('Foi digitado apenas um número ímpar.')
else:
    print(f'Foram digitados {impar} números ímpares.')
