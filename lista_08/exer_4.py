#Remove the line breaks and join the ids in a single line
file = open("ids.txt", "r")
conteudo = file.read()
print(" ".join(conteudo.split()))