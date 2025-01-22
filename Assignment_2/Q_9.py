try:
    num = int(input("Enter a number: "))
    match num % 5:
        case 0:
            print("Remainder is 0")
        case 1:
            print("Remainder is 1")
        case 2:
            print("Remainder is 2")
        case 3:
            print("Remainder is 3")
        case 4:
            print("Remainder is 4")
except ValueError:
    print("Invalid input")
