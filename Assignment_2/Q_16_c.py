n = int(input("Enter n: "))
sum_series = 0
term = 1
sign = 1
for i in range(n):
    sum_series += sign * term
    term += 2
    sign *= -1
print("Sum of series:", sum_series)
