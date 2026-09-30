import random

palavras = ("abacate", "ata", "ananas", "limao", "mangas")

sorteada = random.choice (palavras)

digitada = input ("sua palavra:")
while digitada != sorteada:
    print ("_" *len(sorteada))
    digitada = input ("sua palavra")


