print(" PROGRAMA PARA CALCULAR IRPF ")
print('======================================')
IRPF = 0
SalBruto = float (input ("Digite seu salario em Reais: "))
if  SalBruto < 2428:
    IRPF = 0
elif SalBruto <= 2826.65:
    IRPF = SalBruto * 0.075 - 182.16
elif SalBruto <= 3751.05:
    IRPF = SalBruto * 0.15 - 394.16
elif SalBruto <= 4664.68:
   IRPF = SalBruto * 0.225 - 675.16   
else:
   IRPF = SalBruto * 0.275 - 980.73   
if SalBruto <= 5000:
    IRPF = IRPF - 312.89
elif SalBruto <= 7350:
    IRPF = IRPF - (978.62 - SalBruto * 0.0133145)

if IRPF <= 0:
    IRPF = 0
SalLiq = round (SalBruto - IRPF, 2) 
  
print("Seu imposto é {:.2f}\nSeu salario liquido é {}" .format (IRPF, SalLiq))   
input ("Precione ENTER para sair ....")