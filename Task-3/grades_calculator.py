marks = int(input("Enter your marks [0-100]: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 90:
    print("Grade A - Excellent Performance ")

elif marks >= 80:
    print("Grade B - Very Good Performance ")

elif marks >= 70:
    print("Grade C - Good But Can Do Better")

elif marks >= 50:
    print("Grade D - Average Need To Improve")

else:
    print("Fail-Better Luck Next Time")
