numero = int(input("Digite um número inteiro positivo: "))

original = numero
quant = 0
soma = 0
x = numero

while x > 0:
    quant = quant + 1
    x = x // 10

x = numero

while x > 0:
    digito = x % 10
    soma = soma + digito ** quant
    x = x // 10

if soma == original:
    print("É um número de Armstrong.")
else:
    print("Não é um número de Armstrong.")