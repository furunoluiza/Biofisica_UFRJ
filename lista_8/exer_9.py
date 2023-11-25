arq = open("genomic_dna.txt", "r")
conteudo = arq.read()
exon1 = conteudo[:64]
exon2 = conteudo[90:]
intron = conteudo[64:90]
total = len(conteudo)
codificante = len(exon1 + exon2)
porcentagem = codificante * 100 / total
print("A proporção da sequência codificantes em relação ao tamanho total da sequência é", porcentagem)