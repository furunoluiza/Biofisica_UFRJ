#Print the total sequence highlighting the intron in lowercase letters
file = open("genomic_dna.txt", "r")
content = file.read()
exon1 = content[:64]
exon2 = content[90:]
intron = content[64:90]
print("The sequence highlighting the intron in lowercase letters is: ", 
      content.replace(intron, intron.lower()))