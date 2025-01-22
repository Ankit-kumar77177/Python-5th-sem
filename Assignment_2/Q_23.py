amount = int(input("Enter amount to withdraw: "))
if amount % 10 != 0:
    print("Amount must be a multiple of 10")
else:
    notes_100 = amount // 100
    amount %= 100
    notes_50 = amount // 50
    amount %= 50
    notes_20 = amount // 20
    amount %= 20
    notes_10 = amount // 10
    
    print("100 notes:", notes_100)
    print("50 notes:", notes_50)
    print("20 notes:", notes_20)
    print("10 notes:", notes_10)
