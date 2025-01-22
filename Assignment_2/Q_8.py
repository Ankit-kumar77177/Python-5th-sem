while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        break

if num % 2 == 0:
    result = num * 2
else:
    result = num * num

print("Result:", result)
