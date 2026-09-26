a = int (input("Digite o valor de A, diferente de zero: ")) 
b = int (input("Digite o valor de B: ")) 
c = int (input("Digite o valor de C: ")) 
print ("A Equação é", a,"X^2", b, "X", c)
# Verifica se é uma equação do 2º grau
if a == 0:
    print("O valor de 'a' não pode ser zero.")
    print("A equação não é do 2º grau.")
else:
# Calculo do Delta D=b^2-4ac
    Delta = b * b - 4 * a * c
    print("O Delta é",Delta)
#Calcula das Raizes e verificação das raizes x=(-b+-raiz Delta)/(2*A)
    if Delta < 0:
        print("A Equação não possui raizes reais")
    elif Delta == 0:
        x = -b/(2*a)
        print ("A Raiz é", x)
    else:
        Delta > 0
        x1= (-b + Delta ** 0.5)/(2 * a)
        x2= (-b - Delta ** 0.5)/(2 * a)
        print ("As Raizes são: X1=", x1, "e X2=", x2 )
 