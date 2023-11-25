#Switch to capital letters and print the codons
seq = "atgcgagaatgcatacaagtataacaa"
seq_upper = seq.upper()
codons = seq_upper[0::3]
print(codons)