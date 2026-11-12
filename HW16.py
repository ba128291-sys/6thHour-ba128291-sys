#Name:Bensen Avans
#Class: 6th Hour
#Assignment: HW16


#1. import the "random" library

import random

#2. print "Hello World!"

print("Hello World")

#3. Create three variables named a, b, and c, and allow the user to input an integer for each.

a = float(input("Enter first number: "))
b = float(input("Enter a second number: "))
c = float(input("Enter a third number: "))

#4. Add a and b together, then divide the sum by c. Print the result.

d = (a + b) / c
print(d)

#5. Round the result from #3 up or down, and then determine if it is even or odd.

import math
d = math.floor(d)
if d % 2 == 0:
    print("Its an even number")
else:
    print("Its an odd number")

#6. Create a list of five different random integers between 1 and 10.

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

#7. Print the 4th number in the list.

print(list1[3])

#8. Append another integer to the end of the list, also random from 1 to 10.

list1.append(random.randint(1,10))
print(list1)

#9. Sort the list from lowest to highest and then print the 4th number in the list again.

list1.sort()
print(list1)
print(list1[3])

#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
print("")
i = 1
while i <= 100:
    print(i)
    i += 1

#11. Create a list containing the names of five other students in the classroom.
print("")
student_name_List = ("Owyn" , "Owen" , "Jarrel" , "Malachai", "Misa")
print(student_name_List)

#12. Create a for loop that individually prints out the names of each student in the list.

for student_name_List in student_name_List:
    print(student_name_List)

#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.

print("")
for w in range(1,101):
    print(w)
    if w % 10 == 0:
        break
print("")
#14. Free space. Do something creative. :)

ninety = input("There is more work do you wish to see it? y/n: ")
if ninety == "y":
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")
    print("GO FORTH MY PRINT STATEMENTS AND WREAK HAVOC ON MY TEACHER'S SANITY!!!!!")

else:
    print("You selected 'n' and was spared.")