'''1a Questão: Faça  um  programa,  utilizando  recursão,  que  leia  dos  números  binários,  com  qualquer quantidade
de bits, e em seguida efetue a soma desses dois números binários. Obs.: Não é para converter os números para decimais e
realizar a operação de soma.  Todas as operações devem ser realizadas com números binários.
(Não utilize estrutura de repetição, sob pena de anular a questão). '''


# Atenção: Este código não foi terminado. Esta é a ideia básica, muito obrigado.

def ler_bin(binario, vetor, end, i = 0):
    if i < end:
        vetor.append(int(binario[i]))
        return ler_bin(binario, vetor, end, i + 1)
    else:
        return 0

bina = []
bina2 = []
b1 = input("Digite um número binário:")
b2 = input("Digite outro número binário:")
ler_bin(b1, bina, len(b1))
ler_bin(b2, bina2, len(b2))
print(bina)
print(bina2)
final = []

if len(bina) > len(bina2):
    cont = len(bina)
else:
    cont = len(bina2)


def vetor(cont, final, bina2, bina):
    if bina[len(bina)-1] == 9:
        print('Obrigado por usar nossa calculadora')
        print(final)
        return 0

    else:
        l = bina[cont] + bina2[cont]
        final.append(int(l))
        if final[cont] > 1:
            final[cont] = final[cont] % 2
            print(final)
            if not cont == (len(bina)-1):
                bina[cont + 1] += 1
            else:
                final.append(1)
        bina[cont] = 9
        cont -= 1
        print(cont)
        vetor(cont, final, bina2, bina)



vetor(0, final, bina, bina2)