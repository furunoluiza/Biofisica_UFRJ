#Remove the line breaks and join the ids in a single line
file = open("ids.txt", "r")
content = file.read()
print(" ".join(content.split()))