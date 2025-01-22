limit = int(input("Enter a number: "))
sum_primes = 0

for num in range(2, limit):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_primes += num

print("Sum of prime numbers below", limit, "is", sum_primes)
