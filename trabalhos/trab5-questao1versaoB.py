print('Informe uma matriz de números inteiros.')
matriz = []
soma = 0
linhaM = ""
for i in range(3):
    linha = []
    sominha = 0
    for j in range(3):
        linha.append(int(input(f'Digite o elemento [{i}] [{j}]:')))
        sominha += linha[j]
    matriz.append(linha)
    print(sominha)
    if linhaM == "" and sominha < 0:
        soma = sominha
        linhaM = linha
    elif soma == sominha:
        linhaM = linhaM, linha
    if soma < sominha:
        soma = sominha
        linhaM = linha
    
print('Mais de uma linha pode acabar tendo a maior soma.')
print('Sua matriz é: ')
for i in range(3):
    print(matriz[i])    

print('\nA(s) linha(s) de maior soma é(são):', linhaM, '\nCom a soma de ', soma)