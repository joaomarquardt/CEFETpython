n = 1
menor = 0
while n != 101:
    num = int(input(f'Digite o {n}° número: '))
    if n == 1:
        menor = num
    else:
        if num < menor:
            menor = num
    n += 1
print(f'O menor número digitado foi: {menor}')