# Define a function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get an integer input from the user
user_input = int(input("Enter an integer: "))

# Determine if the number is even or odd
result = check_even_odd(user_input)

# Print the result
print(f"The number {user_input} is {result}.")
