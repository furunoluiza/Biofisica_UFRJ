#Calculate the size of each protein by printing the ID and the function of the protein

file = open("C:/Users/Luiza/OneDrive/Documentos/wsl/Biofísica/CFB126_Biofisica_UFRJ/Trabalho_final/proteinas1.faa", "r")
protein_lines = file.readlines()
protein_united = "\n".join(protein_lines)
protein_list = protein_united.split(">")
for i in protein_list:
    start = i.find("W")
    end = i.find("]")
    id = ">" + i[start:end] + "]"
    seq = len(i[i.find("\n"):])
    print(id, "\n", seq)