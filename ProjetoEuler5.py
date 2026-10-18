numero = 1
divisor = 1
while divisor <= 20:
    if numero % divisor == 0:
        divisor = divisor + 1
    else:
        numero = numero + 1
        divisor = 1
print("O menor número é:", numero)
    