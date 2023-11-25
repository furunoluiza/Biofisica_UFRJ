#Count the number of ocurrences 
#  of the nitrogen bases in the sequence
file = open("dnaQ2.txt", "r")
line = file.readline()
A = line.count("A")
T = line.count("T")
C = line.count("C")
G = line.count("G")
print("Adeninas =", A, "Timinas =", T, 
      "Citocinas =", C, "Guaninas =", G)