arq = open("genomic_dna.txt", "r")
conteudo = arq.read()
exon1 = conteudo[:64]
exon2 = conteudo[90:]
intron = conteudo[64:90]
print("Exon 1 =", exon1)
print("Exon 2 =", exon2)
print("Intron =", intron)
tamanho = len(exon1 + exon2)
print("O tamanho da sequencia codificante é", tamanho)
