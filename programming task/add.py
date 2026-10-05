def add(num1,num2):
      
    try:
        num1 = int(num1) or float(num1)
        num2 = int(num2) or float(num2)
        result  = num1 +  num2
        print(result)
    except ValueError:
       print("Invalid character entered")


num = input("Enter a number: ")
nums = input("Enter a number: ")
print(add(num,nums))



def add(num1, num2):
    return float(num1) + float(num2)


while True:
    num = input("Enter a number: ")
    nums = input("Enter a number: ")
    try:
        print(add(num, nums))
        break
    except ValueError:
        print("invalid character entered")


def to_number(text):
    try:
        return int(text)
    except ValueError:
        return float(text)  # raises ValueError if it isn't a number


def add(first, second):
    return first + second


while True:
    try:
        first = to_number(input("Enter a number: "))
        second = to_number(input("Enter a number: "))
    except ValueError:
        print("invalid character entered")
    else:
        print(add(first, second))
        break