l = list()
soma = 0
q = 0
num = int (input ("digite um numero: "))
while num > 0:
    soma += num
    q += 1
    l.append (num)
    num = int (input ( "digite um numero: "))
media = soma / q
print (l)
print ("A media é:", media)
