bin = []
n10 = int (input ("Digite um numero"))
while n10 > 0:
    x = n10 % 2
    bin.append(x)
    n10 = n10 // 2
bin.reverse() 
print (bin)   
   
