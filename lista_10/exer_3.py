#Insert the IDs strating with the letter "a" into a file, 
#  those that begin with the letter "b" in a second file and other IDs in a new file
Ids = ["ab7a", "bvty", "adf3", "vfg7", "b4f2", "g6hy", "b43c", "zu7d", "bt7u"]
file_rest = open("ids.txt", "w")
file_A = open("ids_starts_wA", "w")
file_B = open("ids_dont_start_wB", "w")
for id in Ids:
    if id.startswith("b"):
        file_rest.write(id + "\n")
    elif id.startswith("a"):
        file_A.write(id + "\n")
    else:
        file_B.write(id + "\n")
file_rest.close()
file_A.close()
file_B.close()