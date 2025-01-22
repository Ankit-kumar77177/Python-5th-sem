# Define a function to determine the type of triangle
def triangle_type(a, b, c):
    # Check if the sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        # Check if the triangle is equilateral
        if a == b == c:
            return "Equilateral"
        # Check if the triangle is isosceles
        elif a == b or a == c or b == c:
            return "Isosceles"
        # If none of the above, the triangle is scalene
        else:
            return "Scalene"
    else:
        return "Not a triangle"

# Get the lengths of the sides from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Determine the type of triangle
triangle = triangle_type(a, b, c)

# Print the result
print(f"The triangle is a {triangle} triangle.")
