num = int(input('Digite um número: '))
total = 1
n = 1
aux = num
while n != aux:
    if n == 1:
        print(num, end=' x ')
        total = num * (num - 1)
        num -= 1
        print(num, end=' x ')
    else:
        num -= 1
        total *= num
        if n < aux - 1:
            print(num, end=' x ')
        else:
            print(num, end=' ')
    n += 1
print(f'= {total}')

