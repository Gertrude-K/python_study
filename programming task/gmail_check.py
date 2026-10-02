def is_valid_email(email):
    return "@" in email and "." in email

user_email = input("Enter your email address: ")
print(is_valid_email(user_email))