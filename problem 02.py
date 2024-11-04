
# Write a Python program that takes an input of average marks from the user and then categorizes the grade as follows:
# If marks are greater than or equal to 90, the grade is "A+."
# If marks are less than 90 but greater than or equal to 70, the grade is "A-."
# If marks are less than 70 but greater than or equal to 50, the grade is "B."
# If marks are less than 50, the grade is "Fail."

avg = float(input("Enter Your Average Marks: "))
if avg >= 90:
    print("Grade is A+")
elif avg >=70:
    print("Grade is: A-")
elif avg >=50:
    print("Grade is: B")
else:
    print("Fail")