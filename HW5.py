#Name: Bensen
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!

print("Hello World")

#1. Create a list with 5 strings containing 5 different names in it.

List1 = ["Foghorn", "Lemon", "Bishop", "Bean", "Beetle"]
print(List1)

#2. Append a new name onto the Name List.

List1.append(input("Give me a name: "))
print(List1)

#3. Print out the 4th name on the list.

print(List1[3])

#4. Create a list with 4 different integers in it.

num_List1 = [12, 300, 929, 123456789]
print(num_List1)

#5. Insert a new integer into the 2nd spot and print the new list.

num_List1.insert(1, 20347)
print(num_List1)

#6. Sort the list from lowest to highest and print the sorted list.

num_List1.sort()
print(num_List1)

#7. Add the 1st three numbers on the sorted list together and print the sum.

num_List1_subsum = num_List1[0] + num_List1[1] + num_List1[2]
print(num_List1_subsum)

#8. Create a list with two strings, two variables, and two boolean values.

List2 = ["Elliot", "Harold", 12, 324, True, True]

#9. Create a print statement that asks the user to input their own index value for the list on #8.

print(List2[int(input("enter index location"))])
