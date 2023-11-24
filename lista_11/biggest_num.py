#Function to return the biggest number between two
def big_num(number_1, number_2):
    if number_1 > number_2:
        return number_1
    else:
        return number_2
number_1 = float(input("Enter a number: "))
number_2 = float(input("Enter another number and I will tell you which is the biggest: "))
print(f'The biggest number is {big_num(number_1, number_2)}.')