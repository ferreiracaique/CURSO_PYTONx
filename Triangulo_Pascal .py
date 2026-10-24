l = [1]
cont = 0
linha = int (input ("digite a quantidades de linha para o triangulo de Pascal: "))
while linha > cont:
    l1 = []
    for p in range(len(l)-1):
        l1.append (l[p] + l[p+1])
    l1 = [1] + l1 + [1]
    print (l1)
    l = l1
    cont += 1 