#Name: Bensen Avans
#Class: 6th Hour
#Assignment: HW13

print("Orange juice is just orange lemonade.")

#1. Import the random function

import random

#2. Create a variable called 'temp' that randomly generates a number between 1 and 30

temp = [random.randint(1,30)]
print(temp)

Twenty = [20]
Ten = [10]

#3. Go to the link below and convert the flowchart into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

#if the temperature is > 20 print it's hot.
#if the temperature is > 10 print it's mild.
#If it's not > 20 or 10 print it's cold.
#Now print in thank you

if temp > Twenty:
    print("It's hot")
elif temp > Ten:
    print("It's mild")
else:
    print("It's cold")

print("Thank you")