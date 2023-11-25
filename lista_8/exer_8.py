arq = open("genomic_dna.txt", "r")
conteudo = arq.read()
exon1 = conteudo[:64]
exon2 = conteudo[90:]
intron = conteudo[64:90]
print("A sequência destacando o intron em letras minusculas é", conteudo.replace(intron, intron.lower()))