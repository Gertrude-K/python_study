def check_login():
    attempt = 3
    count = 0
    
    while attempt > count:
        user_password = input("Enter password: ")
        user_email = input("Enter email: ")
                
        if user_email == "admin@mail.com" and user_password == "Admin@123":
             print("Login is Successful")
             break
        else:
           count += 1 
           print("Invalid username or password")
    else:
         print("Account blocked")
        
          
check_login()