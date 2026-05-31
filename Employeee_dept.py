code=int(input("enter security code "))
if (code==5566):
    dept=str(input("Enter ur department"))
    if(dept.lower()=="finance"):
        access_level =int(input("Enter ur access level"))
        if(access_level>=5):
            print("Access granted ,wlc to meeting room")
        else:
            print("Insufficient acess level")
    else:
        print("Access denied ,Department not allowed")

else:
    print(("Invalid security code"))
