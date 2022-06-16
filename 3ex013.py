#13) Um número perfeito é um número natural para o qual a soma de todos os seus divisores naturais próprios
# (excluindo ele mesmo) é igual ao próprio número. Exemplo 6 é um número perfeito, pois 6 = 1 + 2 +3.
n = int(input('Digite um número para saber se ele é perfeito ou não: '))
aux = aux2 = 1
cont = 0
while aux < n:
    if n % aux == 0:
        cont += aux
    aux += 1
print(cont)
if cont == n:
    print(f'O número {n} é perfeito')
else:
    print(f'O número {n} não é perfeito')