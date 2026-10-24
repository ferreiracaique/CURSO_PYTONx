N1 = float(input("Digite a nota N1: "))
N2 = float(input("Digite a nota N2: "))

MD = (N1 * 2 + N2 * 3) / 5

if MD >= 60:
    print("Aprovado por média")
elif MD >= 20:
    NAF = float(input("Digite a nota da prova final: "))

    MFD1 = (MD + NAF) / 2
    MFD2 = (N1 * 2 + N2 * 3 + NAF * 2) / 7

    if MFD1 >= 60 or MFD2 >= 60:
        print("Aprovado por prova final")
    else:
        print("Reprovado")
else:
    print("Reprovado")