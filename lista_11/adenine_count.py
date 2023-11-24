#Function that counts how many adenines there are in a sequence
def adenines_count(seq):
    upper_seq = seq.upper()
    return upper_seq.count("A")
seq = input("Enter a sequence of nucleic acid: ")
print(f'The number of adenines in the sequence is {adenines_count(seq)}')