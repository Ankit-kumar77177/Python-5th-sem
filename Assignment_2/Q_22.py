def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input("Enter a number: "))
while num > 9:
    num = sum_digits(num)
print("Final single-digit sum:", num)

