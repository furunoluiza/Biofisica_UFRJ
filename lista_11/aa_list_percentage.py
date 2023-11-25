#Function that calculates the percentage of a list of aa in a protein
def aas_percentage(aa_list, seq):
    seq_len = len(seq)
    percentages = []
    i = 0
    while (i < len(aa_list)):
        aminoacid = aa_list[i]
        count_aa = seq.upper().count(aminoacid.upper())
        percentage = (count_aa * 100) / seq_len
        percentages.append(percentage)
        i += 1
    return percentages

aa_list = ["R", "D", "G", "L"]
seq = "RIKELDDRERQVSDELQDLLYQLPNLPAPDVPVGPDETGNVEVKRWGEPRQFAFPVKPHWDLGVAMDGLDFERAAKVTGS"
result = aas_percentage(aa_list, seq)

i = 0
while i < len(aa_list):
    aminoacid = aa_list[i]
    percentage = result[i]
    print(f'The percentage of the amino acid {aminoacid} is {percentage:.2f}%')
    i += 1