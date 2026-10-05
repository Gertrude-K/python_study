# def largest_no(number1, number2, number3, number4):
#     largest = number1
#     if number2 > largest:
#         largest = number2
#     if number3 > largest:
#         largest = number3
#     if number4 > largest:
#         largest = number4
#     return largest

# user_input1 = float(input("Enter the first no: "))
# user_input2 = float(input("Enter the second no: "))
# user_input3 = float(input("Enter the third no: "))
# user_input4 = float(input("Enter the fourth no: "))
# print(largest_no(user_input1,user_input2,user_input3,user_input4))

def largest_no(numbers):
    largest=numbers[0]
    for number in numbers:
     if number > largest:
        largest = number
    return largest

    
numbers = []
for i in range(4): 
 value = float(input("Enter a number: "))    # blank 1: which conversion, and why? int they are numbers
 numbers.append(value)                        # blank 2: which list method? append

print(largest_no(numbers))
