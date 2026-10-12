# solicita um palavra para o usuario
palavra = input ("Digite uma palavra: ").upper()
# solicita um letra para o usuario
# .upper() transforma a palavra em maiuscula
letra = input ("Digite uma letra:  ").upper()

cont = 0
# percorre a lista 
for x in palavra:  
    if x == letra: # testa se a letra na lista (palavra) é iual a letra digitada
        cont += 1
print (palavra)        
print ("A letra ",letra, "ocorre ", cont, "vezes")