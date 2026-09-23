#Name: Bensen Avans
#Class: 6th Hour
#Assignment: HW8

#1. Import the "random" library

import random

#2. print "Hello World!"

print("Hello World")

#3. Create three different variables that each randomly generate an integer between 1 and 10

Num_1 = random.randint(1,10)
Num_2 = random.randint(1,10)
Num_3 = random.randint(1,10)

#4. Print the three variables from #3 on the same line.

print(Num_1, Num_2, Num_3)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.

radintsum = Num_1 + 2
radintsub = Num_2 - 4
radintmul = Num_3 * 1.5

#6. Print each result from #5 on the same line.

print(radintsum, radintsub, radintmul)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6

random_num_List = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
print(random_num_List)

#8. Sort the list in #7 and print it.

random_num_List.sort()
print(random_num_List)

#9. Add together the highest three numbers in the list from #7 and print the result.

random_num_List_subsum = random_num_List[1]+random_num_List[2]+random_num_List[3]
print(random_num_List_subsum)

#10. Create a list with 5 names of other students in this class and print the list.

student_name_List = ["Bensen" , "Owyn" , "Owen" , "Malachai" , "Nisa"]

#11. Shuffle the list in #10 and print the list again.

print(student_name_List)
random.shuffle(student_name_List)
print(student_name_List)

#12. Print a random choice from the list of names from #10.

print(random.choice(student_name_List))