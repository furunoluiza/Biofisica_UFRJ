#Function that calculates the percentage of an aminoacid in a protein
def get_aa_percentage(protein, aa):
    protein = protein.upper()
    aa = aa.upper()
    aa_count = protein.count(aa)
    protein_length = len(protein)
    percentage = aa_count * 100 / protein_length
    return percentage
protein = input("Enter a protein sequence: ")
aa = input("Enter an aminoacid to calculate its percentage in the protein: ")
print(f'The percentage of the {aa} is {get_aa_percentage(protein,aa)}')