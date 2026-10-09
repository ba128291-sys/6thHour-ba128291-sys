#Name:Bensen Avans
#Class: 6th Hour
#Assignment: HW11

import random

#1. Print "Hello World!"

print("Hello world")

#2. Create a list with three variables that each randomly generate a number between 1 and 100

Bensen_Number_List = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

#3. Print the list.

print(Bensen_Number_List)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.

Number1 = Bensen_Number_List[0]
Number2 = Bensen_Number_List[1]
Number3 = Bensen_Number_List[2]

if Number1 > Number2 and Number1 > Number3:
    print("Number1 is greater than 2 and 3.")
elif Number2 > Number1 and Number2 > Number3:
    print("Number2 is greater than 1 and 3.")
else:
    print("Number3 is greater than 1 and 2.")

#5. Tie the result (the largest number) from #4 to a variable called "num".

num = Bensen_Number_List[0]

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if num % 2 == 0:
    print("Number2 is even.")
else:
    print("Number2 is odd.")
    if num % 3 == 0:
        print("Number3 is even.")
    else:
        print("Number3 is odd.")
