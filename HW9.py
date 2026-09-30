#Name: Bensen Avans
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!

print("Hello World")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.

Bensen_Character_Dictionary = {
     "Name" : "Twerp",
     "Species" : "Unidentified",
     "Lucky Numbers" : [12, 20, 9]
 }

#3. Print the keys of the dictionary from #2.

print(Bensen_Character_Dictionary.keys())

#4. Print the values of the dictionary from #2

print(Bensen_Character_Dictionary.values())

#5. Print one of the three numbers from the list by itself

print(Bensen_Character_Dictionary["Lucky Numbers"][1])

#6. Using the update function, add a fourth key to the dictionary and give it a value.

Bensen_Character_Dictionary.update({"Intelligence" : [231]})

#7. Print the entire dictionary from #2 with the updated key and value.

print(Bensen_Character_Dictionary)

#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.

Student_Dictionary = {
    "student_1": {
        "Name": "Owyn",
        "Grade": 10,
        "Gamer": True,
    },
    "student_2": {
        "Name": "Owen",
        "Grade": 12,
        "Gamer": True,
    },
    "student_3": {
        "Name": "Bensen",
        "Grade": 11,
        "Gamer": True,
    },
}


#9. Print the names of all three classmates on the same line.

print(Student_Dictionary)

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.

Student_Dictionary.pop("student_2")
print(Student_Dictionary)