# # Write a program that displays a numbers 1 to 50 inside a list.
numbers = list(range(1, 51))
print(numbers)

# # From 1 above display the ones divisible by 7 or 5 inside a list.
divisible = []
for n in numbers:
    if n % 7 == 0 or n % 5 == 0:
        divisible.append(n)
print(divisible)

# # Find sum and average of values in the range between 10 to 40.
sum_values = sum(range(10, 41))
average_values = sum_values / len(range(10, 41))
print(f"Sum: {sum_values}, Average: {average_values}")

# # Put in a list the first 10 odd numbers between 10 to 50.
odd_numbers = []
for n in range(10, 51):
     if n % 2 == 1:
         odd_numbers.append(n)
     if len(odd_numbers) == 10:
         break
print(odd_numbers)

# # write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number = int(input("Enter a number: "))
lst3 = list(range(1, 11))
for i in lst3:
     print(f"{number}*{i}={number * i}")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
# # write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
even=list(range(1, 51))
count=0
for i in even:
     if i % 2 == 0:
         count += 1
print(f"Total no of even numbers from 1 to 50is: {count}")
ls1 = [ ("Jay", '20'), ("Mo", '30'), ("Mya", '32') ]
# # Display the total quantity of the 3 above
total_quantity = 0
for item in ls1:
    quantity=int(item[1])
    total_quantity += quantity
print(f"Total quantity: {total_quantity}")

# 8.Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked

def password():
    correct_password = "admin@123"
    attempts = 4
    count = 0

    while count < attempts:
        password = input("Enter your password: ")
        if password == correct_password:
            print("Access granted.")
            return
        else:
            count += 1
            rem = attempts - count
            print("Try again.")
            print(f"You have {rem} attempts left.")
            if rem == 0:
                print("Account is blocked.")
                return
