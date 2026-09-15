x = 0
SomaQuad = 0
Soma = 0
QuadSoma = 0
while x <= 100:
    SomaQuad = SomaQuad + x * x
    Soma = Soma + x
    QuadSoma = Soma * Soma
    x = x + 1
print (SomaQuad)
print (QuadSoma)
print (QuadSoma - SomaQuad)
input ("Pressione ENTER para sair") 
