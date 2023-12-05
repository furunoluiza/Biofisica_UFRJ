#Program that calculates genome size and GC content
def GC_percentage(genome):
    genome = genome.upper()
    genome_length = len(genome)
    count = 0
    for nucleotide in genome:
        if nucleotide == "G" or nucleotide == "C":
            count += 1
    percentage_GC = count * 100 / genome_length
    return percentage_GC

def process_genome_file(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    genome = ''.join(lines[1:])
    return genome

file_path = input("Enter the path to the genome file: ")
genome_seq = process_genome_file(file_path)

if genome_seq:
    gc_content = GC_percentage(genome_seq)

if gc_content > 0.65:
    print("The genome length has high GC content.")
elif 0.45 <= gc_content >= 0.65:
    print("The genome has average GC content.")
else:
    print("The genome has low GC content.")