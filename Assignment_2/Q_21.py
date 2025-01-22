n = int(input("Enter a number: "))
factorial = 1
i = 1
while factorial < n:
    i += 1
    factorial *= i
if factorial == n:
    print(n, "is a factorial number")
else:
    print(n, "is not a factorial number")
