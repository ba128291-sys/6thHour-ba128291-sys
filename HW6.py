#Name:Bensen Avans
#Class: 6th Hour
#Assignment: HW6

print("Hello World")

#1. Create a list with 9 different numbers inside.

num_List2 = [12, 32, 52, 72, 92, 1, 20, 2111, 78]

#2. Sort the list from highest to lowest.

num_List2.sort(reverse=True)
print(num_List2)

#3. Create an empty list.

empty_num_List1 = []

#4. Remove the median number from the first list and add it to the second list.

num_List2.pop(4)
empty_num_List1.append(num_List2)

#5. Remove the first number from the first list and add it to the second list.

num_List2.pop(0)
empty_num_List1.append(num_List2)

#6. Print both lists.

print(num_List2)
print(empty_num_List1)

#7. Add the two numbers in the second list together and print the result.

empty_num_List1 = num_List2[4] + num_List2[0]
print(empty_num_List1)

#8. Add the sum from #7 to the first list.

num_List2.append(empty_num_List1)

#9. Sort the first list from lowest to highest and print it.

num_List2.sort()
print(num_List2)
