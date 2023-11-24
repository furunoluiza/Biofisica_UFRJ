#Function that takes two numbers and returns true if the first is a multiple of the second
def multiple(number_1, number_2):
    if number_1 % number_2 == 0:
        return True
number_1 = float(input("Enter a first number, I will check if it is a multiple of the second number: "))
number_2 = float(input("Enter a second number: "))
if multiple(number_1, number_2):
    print(f'{number_1} is a multiple of {number_2}')
else:
    print(f'{number_1} is not a multiple of {number_2}')