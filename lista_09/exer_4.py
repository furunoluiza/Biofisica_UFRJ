#Count how many adenines are in the sequence
count = 0
seq = "ATGGCCATGCATGCAATAAATGC"
for i in seq:
    if (i == "A"):
        count += 1
print(count)