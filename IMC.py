""" PROGRAMA PARA CALCULAR IMC """
peso = float (input ("Digite seu peso em kg "))
altura = float ( input("Digite sua altura em metros "))
imc = round (peso / altura **2, 1)
print ("Seu IMC é: ", imc)
if  imc < 18.5:
    print("Abaixo do peso")
if 18.5 <= imc <= 24.9:
    print("Peso Normal ,saudável")
if 25 <= imc <= 29.9:
    print("Acima do peso")
if 30 <= imc <= 34.9:
    print("Obesidade Grau I")    
if 35 <= imc <= 39.9:
    print("Obesidade Grau II")    
if imc >= 40:
    print("Obesidade Mórbida")   
input ("Precione ENTER para sair ....")