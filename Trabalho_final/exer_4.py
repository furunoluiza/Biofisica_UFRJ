#Size of the fragments cut by the restriction enzymes

def find_enzyme(genome_seq, enzyme_seq):
    if enzyme_seq in genome_seq:
        fragments = genome_seq.split(enzyme_seq)
        if len(fragments) == 2:
            frag_1 = fragments[0]
            frag_2 = fragments[1]
            print(f"The size of the first fragment is {len(frag_1)}")
            print(f"The size of the second fragment is {len(frag_2)}")

def process_genome_file(genome_file):
    file = open(genome_file, "r")
    lines = file.readlines()
    genome_seq = ''.join(lines[1:])
    genome = genome_seq.replace("\n", "")
    return genome

def process_enzyme_file(enzyme_file):
    file = open(enzyme_file, "r")
    line = file.read()
    list = line.split()
    enzyme = list[4]
    return enzyme

genome_file = input("Enter the path to the genome file: ")
enzyme_file = input("Enter the path to the enzyme file: ")
genome_seq = process_genome_file(genome_file)
enzyme_seq = process_enzyme_file(enzyme_file)

if genome_seq and enzyme_seq:
    find_enzyme(genome_seq, enzyme_seq)