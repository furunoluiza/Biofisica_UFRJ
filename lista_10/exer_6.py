arq = open("data.csv", "r")
content = arq.readlines()
for line in content:
    n = line.split(",")
    if "Drosophila simulans" in n[0] or "Drosophila melanogaster" in n[0]:
        print(n[2])