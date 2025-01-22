"""def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        median = numbers[n // 2]
    return median

def calculate_mode(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_frequency = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_frequency]
    return modes

numbers = [1, 2, 3, 2, 3, 4, 4, 4, 5, 4, 5, 6]

mean = calculate_mean(numbers)
median = calculate_median(numbers)
mode = calculate_mode(numbers)

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)"""

from statistics import mean,median,mode
numbers=[1,2,3,2,3,4,5,6,7,8,9,]
mean_value=mean(numbers)
median_value=median(numbers)
print(mean_value)