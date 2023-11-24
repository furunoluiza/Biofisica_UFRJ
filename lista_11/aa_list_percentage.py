#Function that calculates the percentage of a list of aa in a protein
def aas_percentage(aa_list, seq):
    seq_len = len(seq)
    percentages = []
    for aminoacid in aa_list:
        count_aa = seq.upper().count(aminoacid.upper())
        percentage = (count_aa * 100) / seq_len
        percentages.append(percentage)
    return percentages
aa_list = input("Enter a list of aminoacids, to calculate their percentage in the protein: ").split(',')
seq = input("Enter the protein sequence: ")
print(aas_percentage(aa_list,seq))