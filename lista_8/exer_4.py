arq = open("ids.txt", "r")
conteudo = arq.read()
print(" ".join(conteudo.split()))