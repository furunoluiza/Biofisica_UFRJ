arq = open("data.csv", "r")
content = arq.readlines()
for seq in content:
    n = seq.split(",")
    if len(n[1]) >= 90 and len(n[1]) <= 110:
        print(n[2])