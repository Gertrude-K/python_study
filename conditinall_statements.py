if 20 > 10:
    print("20 is greater than 10")
else:
    print("20 is less than 10")

age = 30
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")


if age>= 18 and age <= 60:
    print("Access granted.")
else:
    print("Access denied.")

temperature = 65
if temperature > 30:
    print("It's hot outside.")
else:
    print("It's not that hot outside.")

marks = 78
if marks >50:
    print("You passed the exam.")   
else:
    print("You failed the exam.")

password = input("Enter your password: ")
correct_password = "Admin@254"
check_password = password == correct_password
if check_password:
    print("Access granted.")
else:
    print("Access denied.")

age = int(input("Enter your age: "))
if age > 50:
    print("Senior adult.")
elif age > 20:
    print("Adult.")
elif age > 12:
    print("Teenager.")
else:
    print("Child.")

marks = int(input("Enter your marks: "))
if marks > 80:
    print("You got an A grade.")
elif marks > 70:
    print("You got a B grade.")
elif marks >60:
    print("You got a C grade.")
elif marks > 50:
    print("You got a D grade.")
else:
    print("you got an E")

