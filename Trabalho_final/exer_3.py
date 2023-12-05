#Check how many ATG codons there are in the region 3-4kpb of the genome

def count_met(genome):
    genome = genome.upper()
    region = genome[3000:4000]
    metionine = 0
    i = 0
    j = 0
    while j < 1000:
        j = i + 3
        codon = region[i:j]
        if codon == "ATG":
            metionine += 1
        i += 3
    return metionine

#Another solution:
    #for i in range(0, len(region), 3):
    #    codon = region[i:i+3]
    #    if codon == "ATG":
    #        metionine += 1
    #return metionine

def process_genome_file(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    genome = ''.join(lines[1:])
    return genome

file_path = input("Enter the path to the genome file: ")
genome_seq = process_genome_file(file_path)

if genome_seq:
    metionine = count_met(genome_seq)
    print(metionine)