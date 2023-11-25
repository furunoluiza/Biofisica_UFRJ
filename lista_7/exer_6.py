#List of protein identifier
ID = [
    "AAY66821.1",
    "AAY66759.1",
    "AAY66711.1",
    "AAY66706.1",
    "AAY66703.1",
    "AAY66697.1",
    "AAY66696.1",
    "AAY66682.1",
    "AAY66647.1",
    "AAY66625.1",
    "AAY66623.1",
    "AAY66620.1",
    "AAY66619.1",
    "AAY66616.1",
    "AAY66609.1", 
    "AAY66607.1", 
    "AAY66586.1",
    "AAY66564.1"
]

#Calculate the length of the list
print(f"The length of the list is {len(ID)}")

#Check the presence of identifiers
if "AAY66586.1" in ID:
    print("The protein AAY66586.1 is on the list.")
else:
    print("The protein AAY66586.1 is not on the list.")

#Print the 10º on the list
print(f"The 10º on the list is {ID[10]}.")

#Insert the identifiers in the indicated positions
ID.insert(11, "AAY66967.1")
ID.insert(15, "AAY66880.1")
ID.insert(18, "AAY66874.1")
print(f"The list with new identifiers is: {ID}")