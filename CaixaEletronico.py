valor = int(input("Digite o valor do saque: R$ "))
# Calcula a quantidade de cada cédula/moeda
notas100 = valor // 100
valor = valor % 100
notas50 = valor // 50
valor = valor % 50
notas20 = valor // 20
valor = valor % 20
notas10 = valor // 10
valor = valor % 10
notas5 = valor // 5
valor = valor % 5
notas2 = valor // 2
valor = valor % 2
moedas1 = valor // 1
print("\nQuantidade de cédulas e moedas:")
if notas100 != 0 :
    print("Cédulas de R$ 100,00:", notas100)
if notas50 != 0 :    
    print("Cédulas de R$ 50,00:", notas50)
if notas20 != 0 :        
    print("Cédulas de R$ 20,00:", notas20)
if notas10 != 0 :        
    print("Cédulas de R$ 10,00:", notas10)
if notas5 != 0 :        
    print("Cédulas de R$ 5,00:", notas5)
if notas2 != 0 :        
    print("Cédulas de R$ 2,00:", notas2)
if moedas1 != 0 :        
    print("Cédulas de R$ 1,00:", moedas1)
input ("Precione ENTER para sair ....")
