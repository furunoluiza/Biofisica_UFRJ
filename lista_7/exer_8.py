A = {3, 6, 9, 12, 15, 18, 21, 24, 28, 27}
B = {2, 6, 8, 10, 14, 16, 18, 20, 22, 24}
C = {2, 6, 10, 18, 20}
D = {1, 30, 5, 11, 17, 16, 22, 26}

#Check the intersection and difference between A and B
print(f"The intersection between A and B is: {A.intersection(B)}.")
print(f"The difference between A and B is: {A.difference(B)}.")

#Check whether sets A and B are disjoint from set D
if A.isdisjoint(D):
    print("Set A is disjoint form set D.")
else:
    print("Set A is not disjoint form set D.")

if B.isdisjoint(D):
    print("Set B is disjoint form set D.")
else:
    print("Set B is not disjoint form set D.")

#Return whether the set C is a subset of A and B
if C.issubset(A):
    print("Set C is subset of A.")
else:
    print("Set C isn`t subset of A.")

if C.issubset(B):
    print("Set C is subset of B.")
else:
    print("Set C isn`t subset of B.")

#Add elements to set D
D.add("18")
D.add("23")
D.add("25")
D.add("63")
print(f"The set D with the added elements is: {D}")