#Name: Bensen Avans
#Class: 6th Hour
#Assignment: HW15
from HW6 import empty_num_List1

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.

for b in range(5,0, -1):
    print(b)
    if b == 1:
        print("Hello World")

print(" ")

#2. Create a for loop that counts up and prints only even numbers between 1 and 30.

for e in range(2, 31, +2):
    print(e)
    if e % 2 == 0:
        print("Even")

print(" ")

#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.

for n in range(0, 31):
    if n % 3 == 0:
        continue
    else:
        print(n)

print(" ")

#4. Create a for loop that prints 5 different animals from a list.

animals = ["dog", "cat", "bird", "scorpion", "turtle"]
for s in animals:
    print(s)

print(" ")

#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")

backwards = input("Enter a word of your choosing: ")
txt = backwards[::-1]
print(txt)

print(" ")

#6. Create a list containing 10 integers of your choice and print the list.

number_list = [1,2,3,4,5,6,7,8,9,10]
print(number_list)

#7. Create two empty variables named evenNumbers and oddNumbers.

evenNumbers = []
oddNumbers = []

#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.

e = 0
o = 0
for n in number_list:
    if n % 2 == 0:
        e+=1
    else:
        o+=1

print(e)
print(o)

#9. Create a variable that asks the user for an integer and an empty integer variable.

q = int(input("Enter a number: "))
empty_num_List1 = 0

#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)

r = 1
for y in range(1, q+1):
    r *= y
    print(r)

