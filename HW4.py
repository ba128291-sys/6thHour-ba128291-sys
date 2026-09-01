#Name: Bensen Avans
#Class: 6th Hour
#Assignment: HW4

#1. Print "Hello World!"

print("Hello world")

#2. import the 'math' library

import math

#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.

floatX = float(input("Enter a decimal"))

floatY = float(input("Enter a number"))

#4. Create a variable with the value that is x and y added together.

floataddVofxy = floatX + floatY

#5. Print the variable from #4.

print(floataddVofxy)

#6. Create a variable with the value that is x and y added together, then divide the sum by 3.

Vofxydb3 = floataddVofxy / 3

#7. Print the variable from #6.

print(Vofxydb3)

#8. Create a variable with the value of the square root of y, then print the result.

print(math.sqrt(floatY))

#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.

print(round(floatX))

#10. Use the ceiling function to round x up to the nearest whole number. Print the result.

print(math.ceil(floatX))

#11. Use the floor function to round x down to the nearest whole number. Print the result.

print(math.floor(floatX))