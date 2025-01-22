x = float(input("Enter x: "))
n = int(input("Enter n: "))
sum_series = 1
term = 1
sign = -1
for i in range(1, n+1):
    term *= (x*x) / (2*i * (2*i-1))
    sum_series += sign * term
    sign *= -1
print("Sum of series:", sum_series)
