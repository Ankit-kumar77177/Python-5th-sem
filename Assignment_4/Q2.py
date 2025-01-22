def rotate(a, b, c):
    return b, c, a
a, b, c = 'Doug', 22, 1984
for _ in range(3):
    a, b, c = rotate(a, b, c)
    print(a, b, c)
