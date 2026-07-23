while True:
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        continue

    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if not has_upper:
        print("Password must contain at least one uppercase letter.")
        continue

    print("Password is valid.")
    break


  












     
