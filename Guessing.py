import random
cnumber = random.randrange(1,100)
usernumber = int(input("Enter the no : "))
if usernumber>cnumber:
    print("computer no is : ",cnumber)
    print("Guessing no is high")
elif cnumber>usernumber:
    print("computer no is: ",cnumber)
    print("Guessing no is low")
else:
    print("guess no is equal")
