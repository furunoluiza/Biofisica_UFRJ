#First tuple of aminoacids
tuple_1 = ('R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L',
             'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V')

#Calculate the length of the tuple
print(f"The length of aminoacids is {len(tuple_1)}.")

#Check if glutamic acid is on the list
if ("E" in tuple_1):
    print("Glutamic acid is on the list")
else:
    print("Glutamic acid is not on the list")

#Second tuple of aminoacids
tuple_2 = ('Histidina (H)', 'Triptofano (W)','Tirosina (Y)',
            'Prolina (P)', 'Serina (S)')

#Concatenate the tuples
united_tuples = tuple_1 + tuple_2
print (f"The new tuple is: {united_tuples}")

#Count the ocurrence of W, N and C
W = united_tuples.count("Triptofano (W)")
N = united_tuples.count("N")
C = united_tuples.count("C")
print (f"The number of ocurrance of W is {W}")
print (f"The number of ocurrance of N is {N}")
print (f"The number of ocurrance of C is {C}")

#Return the position of the first element Asparagine(N)
i = united_tuples.index("N")
print(f"The index of asparagine on the list is {i}.")

#Return the last 5 elements of the tuple
len = len(united_tuples)
last_5 = united_tuples[len - 5:len]
print(f"The last 5 elements are: {last_5}.")