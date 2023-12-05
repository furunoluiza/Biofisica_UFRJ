#Print only the sequences without the headers

file = open("C:/Users/Luiza/OneDrive/Documentos/wsl/Biofísica/CFB126_Biofisica_UFRJ/Trabalho_final/proteinas1.faa", "r")
proteins = file.readlines()
for line in proteins:
    if not line.startswith(">"):
        print (line.strip())
file.close()