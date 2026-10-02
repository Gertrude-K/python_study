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



password()