arq = open("dnaQ2.txt", "r")
line = arq.readline()
A = line.count("A")
T = line.count("T")
C = line.count("C")
G = line.count("G")
print("Adeninas =", A, "Timinas =", T, "Citocinas =", C, "Guaninas =", G)