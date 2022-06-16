#23)Um comerciante comprou um produto que quer vende-lo com um  lucro de 45%  se o valor da
# compra for menor que 20 BRL caso contrário o lucro será de 30%.
# Entre com o valor do produto e imprima o valor de venda.
n = float(input('Digite o valor do produto: R$'))
if n < 20:
    n = n * 145 / 100
elif n >= 20:
    n = n * 130 / 100
print(f'O valor de venda será de R${n:.2f}')