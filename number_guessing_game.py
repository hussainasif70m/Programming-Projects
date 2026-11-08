# Number guessing game

import random
Cnumber=random.randrange(1,101)
Unumber=int(input("Enter your number :--"))
if Cnumber > Unumber:
    print("computer number",Cnumber)
    print("your number is low")
elif Unumber > Cnumber:
    print("computer number", Cnumber)
    print("your number is high")
else:
    print("computer number", Cnumber)
    print("your number is equal")