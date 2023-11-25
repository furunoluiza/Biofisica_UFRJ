#Insert into a file IDs that begin with the letter "b" 
#  and in another file IDs that do not begin with "b"
Ids = ["ab7a", "bvty", "adf3", "vfg7", "b4f2", "g6hy", "b43c", "zu7d", "bt7u"]
file_1 = open("Ids.txt", "w")
file_2 = open("Ids_withoutb.txt", "w")
for id in Ids:
    if id.startswith("b"):
        file_1.write(id + "\n")
    else:
        file_2.write(id + "\n")
file_1.close()
file_2.close()