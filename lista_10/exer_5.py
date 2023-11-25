#Print IDs that start with the letter "b" and do not end with "2"
Ids = ["ab7a", "bvty", "adf3", "vfg7", "b4f2", "g6hy", "b43c", "zu7d", "bt7u"]
for id in Ids:
    if id.startswith("b") and not id.endswith("2"):
        print(id)