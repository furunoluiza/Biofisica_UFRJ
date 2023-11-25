#Proportion of the coding sequence
#  in relation to the total size of the sequence
file = open("genomic_dna.txt", "r")
seq = file.read()
exon1 = seq[:64]
exon2 = seq[90:]
intron = seq[64:90]
total = len(seq)
coding = len(exon1 + exon2)
percentage = coding * 100 / total
print("The proportion of the coding sequence in relation \
      to the total sequence size is", percentage)