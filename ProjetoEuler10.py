soma = 0
numero = 2

while numero < 1000:
    divisor = 2
    quantidade_divisores = 0

    while divisor < numero:
        if numero % divisor == 0:
            quantidade_divisores = quantidade_divisores + 1

        divisor = divisor + 1

    if quantidade_divisores == 0:
        soma = soma + numero

    numero = numero + 1

print("A soma dos números primos abaixo de 1000 é:", soma)