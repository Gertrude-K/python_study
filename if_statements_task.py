# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
input3 = int(input("Enter the third number: "))

if input1 >= input2 and input1 >= input3:
    print(input1)
elif input2 >= input1 and input2 >= input3:
    print(input2)
else:
    print(input3)

# 2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temperature = float(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("The temperature is too high")
elif temperature > 15:
    print("Normal temperature")
else:
    print("Cold temperature")
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password = input("Enter your password: ")
correct_password = "secret123"
check_password = password == correct_password
if check_password:
    print("Access granted")
else:
    print("Access denied")

# 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# If start_date comes before end_date, print "Valid period",

# If start_date is after end_date, print "Invalid period".
# If both dates are the same, print "One-day period".
# 2.Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length".
start_date = '2024-01-01'
end_date = '2024-12-31'

if start_date < end_date:
    print("Valid period")
elif start_date > end_date:
    print("Invalid period")
else: 
    print("One-day period")


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")           

if len(str1) > len(str2):
    print("str1 is longer")
elif len(str2) > len(str1):
    print("str2 is longer")
else:
    print("Both are of equal length")



# 3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# Prints "Access Granted" if user_id is in valid_ids.
# Prints "Access Denied" if user_id is not in valid_ids.
valid_ids = [101, 102, 103]
user_id = 105

if user_id in valid_ids:
    print("Access Granted")
else:
    print("Access Denied")
# 4.Given a variable value that could be of any type, write a conditional statement that:
# Prints "String Detected" if value is a string.
# Prints "Integer Detected" if value is an integer.
# Prints "Unknown Type" for any other type.
variable = "hello"
if type(variable) == str:
    print("String Detected")
elif type(variable) == int:
    print("Integer Detected")
else:
    print("Unknown Type")   
