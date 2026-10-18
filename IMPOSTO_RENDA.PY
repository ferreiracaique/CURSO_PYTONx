print(" PROGRAMA PARA CALCULAR IRPF ")
print('======================================')
IRPF = 0
SalBruto= float (input ("Digite seu salario em Reais: "))
if  SalBruto < 2428:
    IRPF = 0
if 2424.81 <= SalBruto < 2826.65:
    IRPF = SalBruto * 0.075 - 182.16
if 2826.65 <= SalBruto < 3751.05:
    IRPF = SalBruto * 0.15 - 394.16
if 3751.06 <= SalBruto < 4664.68:
   IRPF = SalBruto * 0.225 - 675.16   
if 4664.69 <= SalBruto:
   IRPF = SalBruto * 0.275 - 980.73   
SalLiq = round (SalBruto - IRPF, 2) 
  
print("Seu imposto é {}\nSeu salario liquido é {}" .format (IRPF, SalLiq))   
input ("Precione ENTER para sair ....")