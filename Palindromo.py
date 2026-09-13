Numero = int (input ("Digite um numero "))
print ("O numero digitado é", Numero)
original = Numero
inverso = 0
# Inverte o número usando operações matemáticas
while Numero > 0:
    digito = Numero % 10
    inverso = inverso * 10 + digito
    Numero = Numero // 10
if original == inverso: 
    print("O número é um palíndromo.") 
else: 
    print("O número NÃO é um palíndromo.")

input ("Precione ENTER para sair ....")