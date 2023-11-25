#Program that takes three fastas sequences and writes them to a file
sequence_1 = "TTTGAAGGCTAATGAAAAAGCAGATTT"
sequence_2 = "agcattttggtggtgatttggaaagggtgt"
sequence_3 = "GCGC-GGTCATC-ATTATCGG-CTTTGTG---TCGGGC"
seq_2 = sequence_2.replace(sequence_2, sequence_2.upper())
seq_3 = sequence_3.replace('-', '')
file = open("sequencias_fasta", "w")
file.write(">VC1458" "\n" + sequence_1 + "\n")
file.write(">BK4320" "\n" + seq_2 + "\n")
file.write(">SP3450" "\n" + seq_2)
file.close()
new = open("sequencias_fasta", "r")
content = new.read()
print(content)