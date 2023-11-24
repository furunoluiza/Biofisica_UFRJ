#Function to return if a number is even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
number = float(input("Enter a number to check if it is even or odd: "))
print(f"The number {number} is {even_or_odd(number)}")