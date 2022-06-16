print('Informe uma matriz de números inteiros.')
matriz = []
soma = 0
linhaM = ""
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'Digite o elemento [{i}] [{j}]:')))
    matriz.append(linha)
    if linhaM == "" and sum(linha) < 0:
        soma = sum(linha)
        linhaM = linha
    elif soma == sum(linha):
        linhaM = linhaM, linha
    if soma < sum(linha):
        soma = sum(linha)
        linhaM = linha

print('Mais de uma linha pode acabar tendo a maior soma.')
print('Sua matriz é: ')
for i in range(3):
    print(matriz[i])    

print('\nA(s) linha(s) de maior soma é(são):', linhaM, '\nCom a soma de ', soma)