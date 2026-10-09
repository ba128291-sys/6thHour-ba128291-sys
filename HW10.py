#Name:Bensen Avans
#Class: 6th Hour
#Assignment: HW10

import random

#1. Print "Hello World!"

print("Hello World")

#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.

VarA = random.randint(1, 10)
VarB = random.randint(1, 10)
VarC = random.randint(1, 10)

#3. Print A, B, and C on the same line.

print(VarA, VarB, VarC)

#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.

if VarA < 5:
    print("Less than 5")
elif VarA > 5:
    print("Greater than 5")
else:
    print("Equal to 5")

#5. Make an if statement that prints if variable B is between 3 and 7, or not.

if 3 < VarB < 7:
    print("In between 3 and 7")
else:
    print("Not between 3 and 7")

#6. Make an if statement that prints if variable C is even or odd.

if VarC % 2 == 0:
    print("Even")
else:
    print("Odd")

#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20

VarD = 3 + random.randint(1, 20)
print(VarD)

#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.

if VarD < VarA:
    print("Less than VarA")
elif VarD > VarA:
    print("Greater than VarA")
else:
    print("Equal to VarA")

if VarD < VarB:
    print("Less than VarB")
elif VarD > VarB:
    print("Greater than VarB")
else:
    print("Equal to VarB")

if VarD < VarC:
    print("Less than VarC")
elif VarD > VarC:
    print("Greater than VarC")
else:
    print("Equal to VarC")