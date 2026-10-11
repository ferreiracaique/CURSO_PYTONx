l = list()
soma = 0
q = 0
print("--------------------------------------------------------------------------")
print("NESSE PROGRAMA VOCE IRÁ DIGITAR UM CONJUNTO DE NUMEROS MAIORES QUE ZERO")
print("PARA FINALIZAR O CONJUNTO DIGITE ZERO")
print("--------------------------------------------------------------------------")
print()
input(print("TECLE ENTER PARA INICIAR O PROGRAMA"))
print()

num = int (input ("digite um numero inteiro: "))
while num > 0:
    soma += num
    l.append (num)
    num = int (input ( "digite um numero inteiro: "))

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
print ("O menor numero é: ",menor)
pares = 0
for p in range (len(l)-1):
    if l[p] < l[p+1]:
        pares += 1

print(pares)