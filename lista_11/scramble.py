#Function that takes a string and returns another string with the characters scrambled
import random
def scrambled(string):
    caracters = list(string)
    random.shuffle(caracters)
    string_scrambled = ''.join(caracters)
    return (string_scrambled)
string = input("Enter a string and I will scramble it: ")
print(scrambled(string))