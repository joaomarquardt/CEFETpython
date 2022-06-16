'''2a Questão: Um subvetor de um vetor v é o que sobra depois de alguns dos elementos de v são apagados.
Por exemplo:
12  13  10  3 é um subvetor de 11  12  13  11  10  9  7  3  3, mas não é um subvetor de 11  12  10  11  13  9  7  3  3.
Faça um programa que leia dois vetores de inteiros, um vetor ve um vetor x, e em seguida decida se o vetor x é um
subvetor de v. Peça para o usuário entrar com os tamanhos do vetor v e do vetor x.
Obs.: O tamanho do vetor x não pode ser maior que o vetor v.
'''

while True:
     tamanho_v = int(input("Digite o tamanho do vetor V: "))
     tamanho_x = int(input("Digite o tamanho do vetor X: "))
     if tamanho_x > tamanho_v:
          print("\n X não pode ser maior que V. Tente novamente.")
     else:
          break
v = []
x = []
for c in range(0, (tamanho_v)):
     v.append(int(input('')))
for c in range(0, (tamanho_x)):
     x.append(int(input('')))
dado = []
for c in range(0, tamanho_v):
     if v[c] in x:
          dado.append(v[c])
n = 0
lista = []
for c in range(len(dado)):
     if lista == x:
          break
     else:
          if dado[c] == x[n]:
               lista.append(dado[c])
               n += 1
if lista == x:
     print("O vetor X é subvetor do vetor V.")
else:
     print("O vetor X não é subvetor do vetor V.")