def get_grade(marks):

        if marks >= 80:
                return "A"
        elif marks >= 60 :
                return "B"
        elif marks >= 50:
                return "C"
        elif marks >= 40:
                return "D"
        else:
                return "E"
   

while True:
    try:
        marks = int(input("Enter your marks: "))
        if marks in range(0, 101):
            break
        else:
            print("Please enter a valid number between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

grade = get_grade(marks)
print(f"Your grade is: {grade}")
 