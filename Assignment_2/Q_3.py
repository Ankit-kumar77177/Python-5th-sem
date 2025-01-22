score = int(input("Enter the student's score: "))

if score >= 90:
    print("Grade: A")
    print("Comment: Excellent")
elif score >= 80:
    print("Grade: B")
    print("Comment: Good")
elif score >= 70:
    print("Grade: C")
    print("Comment: Average")
elif score >= 60:
    print("Grade: D")
    print("Comment: Needs Improvement")
else:
    print("Grade: F")
    print("Comment: Failing")
