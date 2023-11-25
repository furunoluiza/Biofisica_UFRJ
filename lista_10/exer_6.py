#Print the third column of the species 
#  _Drosophila melanogaster_ or _D.simulans_
file = open("data.csv", "r")
content = file.readlines()
for line in content:
    n = line.split(",")
    if "Drosophila simulans" in n[0] or "Drosophila melanogaster" in n[0]:
        print(n[2])