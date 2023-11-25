# Calculate the size of the sequence
file = open("dnaQ2.txt", "r")
lines = file.readlines()
for i in lines:
    print(len(i))