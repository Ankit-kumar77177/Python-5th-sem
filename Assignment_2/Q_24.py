num = input("Enter a number: ")
digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
for digit in num:
    print(digits[int(digit)], end=" ")
print()