#Print the exon sequences and then join all the sequences

genome_file = open("C:/Users/Luiza/OneDrive/Documentos/wsl/Biofísica/CFB126_Biofisica_UFRJ/Trabalho_final/genoma1.fna", "r")
exon_file = open("C:/Users/Luiza/OneDrive/Documentos/wsl/Biofísica/CFB126_Biofisica_UFRJ/Trabalho_final/exons1", "r")
genome_lines = genome_file.readlines()
exons_lines = exon_file.readlines()
sequence = ''.join(genome_lines[1:])
genome = sequence.replace("\n", "")
for exon in exons_lines:
    start_stop = exon.split(",")
    start = int(start_stop[0])
    stop = int(start_stop[1])
    print(f"The coding sequence is {genome[start:stop]}\n")