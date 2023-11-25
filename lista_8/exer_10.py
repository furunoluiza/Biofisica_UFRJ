sequencia_1 = "TTTGAAGGCTAATGAAAAAGCAGATTT"
sequencia_2 = "agcattttggtggtgatttggaaagggtgt"
sequencia_3 = "GCGC-GGTCATC-ATTATCGG-CTTTGTG---TCGGGC"
seq_2 = sequencia_2.replace(sequencia_2, sequencia_2.upper())
seq_3 = sequencia_3.replace('-', '')
arq = open("sequencias_fasta", "w")
arq.write(">VC1458" "\n" + sequencia_1 + "\n")
arq.write(">BK4320" "\n" + seq_2 + "\n")
arq.write(">SP3450" "\n" + seq_2)
arq.close()
new = open("sequencias_fasta", "r")
conteudo = new.read()
print(conteudo)