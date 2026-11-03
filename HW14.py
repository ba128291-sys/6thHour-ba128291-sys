#Name: Bensen Avans
#Class: 6th Hour
#Assignment: HW14
import random

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.

i = 5
while i > 0:
    print(i)
    i -= 1
else:
    print("Hello World")

print(" ")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).

b = 1
while b < 30:
    b += 1
    if b % 2 == 0:
        print(b)

print(" ")
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.

e = 1
while e < 30:
    e += 1
    if e % 3 == 0:
        print(e)

print(" ")
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.

while True:
    n = random.randint(1, 6)
    print(n)
    if n == 1:
        break

#5. Create a while loop that asks for a number input until the user inputs the number 0.

while True:
    a = int(input("Input the number 0: "))
    if a == 0:
        break