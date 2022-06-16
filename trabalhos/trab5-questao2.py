numero = 0
matriz = []
while not 101 > numero > 0:
    numero = int(input('Informe o tamanho da matriz quadrada A. O máximo será 100.'))

    if not 101 > numero > 0:
        print('Insira um valor válido.')
        
for i in range(numero):
    linha = []
    for j in range(numero):
        linha.append(int(input(f'Digite o elemento [{i}] [{j}]:')))
    matriz.append(linha)

print('A matriz A, que você digitou, é: ')
for i in range(numero):
    print(matriz[i])

transposta =[]

for i in range(numero):
    linha=[]
    for j in range(numero):
        linha.append(matriz[j][i])
    transposta.append(linha)

print('\nA matriz AT, transposta da matriz A, é: ')
for i in range(numero):
    print(transposta[i])