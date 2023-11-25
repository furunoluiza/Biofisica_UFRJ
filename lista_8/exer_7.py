#Print the exons and introns in the sequence
# and find the size of the coding sequence
file = open("genomic_dna.txt", "r")
seq = file.read()
exon1 = seq[:64]
exon2 = seq[90:]
intron = seq[64:90]
print("Exon 1 =", exon1)
print("Exon 2 =", exon2)
print("Intron =", intron)
size = len(exon1 + exon2)
print("The size of the coding sequence is", size)