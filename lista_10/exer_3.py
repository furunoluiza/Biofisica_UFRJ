Ids = ["ab7a", "bvty", "adf3", "vfg7", "b4f2", "g6hy", "b43c", "zu7d", "bt7u"]
arq_rest = open("ids.txt", "w")
arq_A = open("ids_starts_wA", "w")
arq_B = open("ids_dont_start_wB", "w")
for id in Ids:
    if id.startswith("b"):
        arq_rest.write(id + "\n")
    elif id.startswith("a"):
        arq_A.write(id + "\n")
    else:
        arq_B.write(id + "\n")
arq_rest.close()
arq_A.close()
arq_B.close()