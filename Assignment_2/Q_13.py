position = input("Enter chess position (e.g., a1): ")
column = position[0]
row = int(position[1])

if (ord(column) - ord('a') + row) % 2 == 0:
    print("Black")
else:
    print("White")

