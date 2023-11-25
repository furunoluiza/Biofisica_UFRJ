#Create a file and enter your name and age, check if it worked
file = open("apresentacao.txt", "w")
file.write("Luiza Furuno Machado" "\n" "21 anos")
file.close()
new = open("apresentacao.txt", "r")
read = new.read()
print(read)