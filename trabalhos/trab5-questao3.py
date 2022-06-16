print('Serão pedidas informações sobre a corrida. Diga o seguinte:\n')
matriz = []
melhorVolta = []
melhorVoltaT = 0
melhorVoltista = []
contador = 0
auxDois = 0
corredor = 0

for i in range(2):
    corredor += 1
    contador = 0
    linha = []
    linha.append(input(f'Informe o nome do corredor {corredor}: '))
    for j in range(2):
        contador += 1
        linha.append(int(input(f'Informe o tempo da volta {contador} dele, em segundos: ')))
        auxDois = int(linha[contador])
        if melhorVoltaT == 0:
            melhorVolta = contador
            melhorVoltaT = auxDois
            melhorVoltista = linha[0]
        elif melhorVoltaT == auxDois:
            melhorVoltista = melhorVoltista, linha[0]
            melhorVolta = melhorVolta, contador
        if auxDois < melhorVoltaT:
            melhorVolta = contador
            melhorVoltaT = auxDois
            melhorVoltista = linha[0]
    matriz.append(linha)
        
        

print('A corrida teve os seguintes resultados: ')
for i in range(2):
    print(matriz[i])    

print('Quem teve a melhor volta da prova:', melhorVoltista, '\nEle(s) teve(tiveram) essa volta na:', melhorVolta)
print('Não foi possivel realizar as outras tarefas da questão.')
