number=int(input('enter your registration number :'))
if number==1221:

    sub=str(input("Enter ur subject :"))
    if sub.lower()=='python':
        pwd=int(input("enter your password :"))

        if pwd==8888:
            print("Login successful")
        else:
            print("Wrong password")
    else:
        print("Sub not avlbl")

else:
    print("Registration failed")
