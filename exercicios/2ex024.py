#4) Faça um programa que leia nome, nota 1 e nota 2 de um aluno. Em seguida calcule a média e informe se o
# aluno está aprovado reprovado ou em prova final. A média maior ou igual a 7 é aprovação menor que 3 a reprovação
# e demais casos o aluno está em prova final.
nome = str(input('Digite seu nome: ')).strip().title()
n1 = float(input('Digite sua 1ª nota: '))
n2 = float(input('Digite sua 2ª nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('VOCÊ ESTÁ APROVADO!')
elif 3 <= media < 7:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO E FARÁ PROVA FINAL!')
else:
    print('VOCÊ ESTÁ REPROVADO!')
    