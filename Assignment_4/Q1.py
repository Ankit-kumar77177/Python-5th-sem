import random

N = int(input("Enter the size of the list: "))
numbers = [random.randint(1, 100) for _ in range(N)]
total_sum = sum(numbers)
average = total_sum / N

print("List:", numbers)
print("Sum:", total_sum)
print("Average:", average)
