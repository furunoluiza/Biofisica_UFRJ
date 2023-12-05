#Recover region 3-4kpb of the genome
#Print the complementary sequence

def genome_cut(genome):
    genome = genome.upper()
    region = genome[3000:4000]
    comp_seq = []
    for nucleotide in region:
        if nucleotide == "A":
            comp_seq.append("T")
        elif nucleotide == "T":
            comp_seq.append("A")
        elif nucleotide == "C":
            comp_seq.append("G")
        else:
            comp_seq.append("C")
    return ''.join(comp_seq)
        

def process_genome_file(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    genome = ''.join(lines[1:])
    return genome

file_path = input("Enter the path to the genome file: ")
genome_seq = process_genome_file(file_path)

if genome_seq:
    comp_seq = genome_cut(genome_seq)
    print(comp_seq)