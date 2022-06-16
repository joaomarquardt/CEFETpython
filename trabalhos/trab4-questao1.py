'''1a Questão: Faça um programa que preencha um vetor com vários valores inteiros lidos do teclado. A condição de parada
será o usuário digitar FIM. Em seguida, informe o número de ocorrências de cada elemento do vetor.
Ex.: Vet = [1, -100, 1, 30, 12, 1, 12, 12, 12, 90] Seu programa deverá retornar:
O número -100 apareceu 1 vez no vetor
O número 1 apareceu 3 vezes no vetor
O número 12 apareceu 4 vezes no vetor
O número 30 apareceu 1 vez no vetor
O número 90 apareceu 1 vez no vetor
Obs.:  Cada ocorrência do número no vetor, só deve aparecer uma vez na resposta, ou seja, não é para o seu programa
informar 3 vezes que o número 1 apareceu no vetor, e nem para informar que o número 12 apareceu 4 vezes no vetor. '''

print("Diga os números que deseja colocar no vetor.\nPara terminar, diga FIM.")

vetor = []
contador = 0
resposta = 0

vetor.append(input())

while vetor[contador] != 'FIM':
    vetor.append(input())
    contador += 1
    
    
print ("Seu vetor é", vetor)

pedido = input("Qual número gostaria de achar?\n")

if pedido == "":
    print ("Não se foi pedido nada para se procurar.\n")
else:
    while len(vetor) > 0:
        if vetor[0] == pedido:
            resposta += 1
        vetor.pop(0)
        
    if resposta == 1:
        print("O número", resposta, " aparece 1 vez na lista.\n")
    else:
        print("O número ", pedido, " aparece ", resposta, " vezes na lista.\n")

print("Acabou cambada!")    