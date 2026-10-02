def find_largest(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number1 and number2 >= number3:
        return number2
    else:
        return number3
    
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
largest_number = find_largest(number1, number2, number3)
print(f"The largest number among {number1}, {number2}, and {number3} is: {largest_number}")

def find_largest(number1, number2, number3):
    largest_number = number1
    if number2 > largest_number:
        largest_number = number2
    if number3 > largest_number:
        largest_number = number3
    return largest_number

def find_largest(numbers):
    largest = numbers[0]
    for n in numbers[1:]:
        if n > largest:
            largest = n
    return largest

print(find_largest([4, 9, 2]))