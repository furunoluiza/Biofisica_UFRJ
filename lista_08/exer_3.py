#Difference between readlines and realine
file = open("ids.txt", "r")
readlines = file.readlines()
readline = file.readline()
print(f"The readlines return is: {readlines}.")
print(f"The readline return is: {readline}.")

# The readline method prints only the first 
# line of the file and the readlines method 
# prints all lines of the file.
