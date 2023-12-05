#Program that prints the start and stop codons

def codons(lines):
    for line in lines:
        codon = line.strip().split(',')
        print(f"O start codon é {codon[0]}, o stop codon é {codon[1]}")


def process_exon_file(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    return lines

file_path = input("Enter the path to the exon file: ")
lines = process_exon_file(file_path)

if lines:
    output = codons(lines)