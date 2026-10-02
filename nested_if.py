# series of conditional statement inside a conditinal statement is called nested conditional statement.
age = int(input("Enter your age: "))

if age >= 18:
    licence = input("Do you have a driving licence? (yes/no): ")
    if licence.lower() == "yes":
        print("You are eligible to drive.") 
    else:
        print("You are not eligible to drive without a licence.")
else:
    print("You are too young to drive.")

 # Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."

credit_score = int(input("Enter credit score: "))
annual_income = float(input("Enter annual income: "))

if credit_score > 700:
    if annual_income > 50000:
      print("Loan Approved.")
    else:
        print("Income requirement not met.")
else: 
    print("Credit score too low")



