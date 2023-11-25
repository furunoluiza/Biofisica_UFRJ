#Print the total sequence highlighting the intron in lowercase letters
arq = open("genomic_dna.txt", "r")
conteudo = arq.read()
exon1 = conteudo[:64]
exon2 = conteudo[90:]
intron = conteudo[64:90]
print("The sequence highlighting the intron in lowercase letters is: ", 
      conteudo.replace(intron, intron.lower()))