valores = []
posmaior = []
posmenor = []
n = 0
maior = menor = 0
for c in range(0, 6):
    for c2 in range(0, 3):
        valores.append(float(input(f'Digite um valor para [{c, c2}]: ')))
        if c == 0 and c2 == 0:
            posmaior = [c, c2]
            posmenor = [c, c2]
            maior = valores[-1]
            menor = valores[-1]
        else:
            if valores[-1] > maior:
                maior = valores[-1]
                posmaior = [c, c2]
            if valores[-1] < menor:
                menor = valores[-1]
                posmenor = [c, c2]
print('-=' * 20)
print('         1   |    2   |    3   ')
a = 1
print(a, end='  | ')
for numeros in range(0, len(valores)):
    n += 1
    if n != 3:
        print(f'[{valores[numeros]:^7}]', end='')
    else:
        print(f'[{valores[numeros]:^7}]')
        a += 1
        if a < 7:
            print(a, ' | ', end='')
    if n == 3:
        n = 0
print('-=' * 20,
      f'\nO maior valor é: {maior} e se encontra na linha {posmaior[0] + 1} e coluna {posmaior[1] + 1}',
      f'\nO menor valor é: {menor} e se encontra na linha {posmenor[0] + 1} e coluna {posmenor[1] + 1}')