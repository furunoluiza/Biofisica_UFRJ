#Print the identifiers that cotain
#  the sequences between 90 and 110 nucleotides
file = open("data.csv", "r")
content = file.readlines()
for seq in content:
    n = seq.split(",")
    if len(n[1]) >= 90 and len(n[1]) <= 110:
        print(n[2])