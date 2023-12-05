#Print only the identifier and function of the protein

file = open("C:/Users/Luiza/OneDrive/Documentos/wsl/Biofísica/CFB126_Biofisica_UFRJ/Trabalho_final/proteinas1.faa", "r")
proteins = file.readlines()
for line in proteins:
    if line.startswith(">"):
        print (line)