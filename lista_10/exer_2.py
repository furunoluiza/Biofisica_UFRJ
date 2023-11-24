Ids = ["ab7a", "bvty", "adf3", "vfg7", "b4f2", "g6hy", "b43c", "zu7d", "bt7u"]
arq_1 = open("Ids.txt", "w")
arq_2 = open("Ids_withoutb.txt", "w")
for id in Ids:
    if id.startswith("b"):
        arq_1.write(id + "\n")
    else:
        arq_2.write(id + "\n")
arq_1.close()
arq_2.close()