l = list()
soma = 0
q = 0
num = int (input ("digite um numero: "))
while num > 0:
    soma += num
    l.append (num)
    num = int (input ( "digite um numero: "))
media = soma / len(l)
print ("os numrros digitados foram", l)
print ("A media é:", media)
soma  = 0
# para calcular variancia ((n1-media)^2 + ... + (n-media)^2)/n
for num in l:
    soma = soma + (num - media)**2
variancia = soma / len(l)
print( "A Variancia é: ", variancia)
maior = l [0]
for x in l:
    if x > maior:
        maior = x
print ("O maior numero é: ",maior)
menor = l [0]
for x in l:
    if x < menor:
        menor = x
print ("O maior numero é: ",menor)
