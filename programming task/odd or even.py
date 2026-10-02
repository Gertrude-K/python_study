def check_divisible(number):
    result = "even" if number % 2 == 0 else "odd"
    if number % 4 == 0:
        result += " and divisible by 4"
    return result

while True:
    try:
        user_input = int(float(input("Enter a number: ")))
        break
    except ValueError:
        print("Invalid input please enter a valid number.")
print(F"The number{user_input} is {check_divisible(user_input)}")


