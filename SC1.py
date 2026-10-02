#Name: Bensen Avans
#Class: 6th Hour
#Assignment: Scenario 1
print("")
print("Hello World or person (most likely my teacher) reading the code in this file")
print("")
print(" This a game that takes place in a weird dimension.")
print("The enemies here work under a kind of a 'Alice in Wonderland' behaviour.")
print("For this scenario I have only selected five enemies from island one.")
print("Island one is a strange jungle made with or out of real world instruments.")
print("Instead of character lore, I have been told I needed to put down stats for the monsters")
print("                                           -Bensen Avans, head of character development")
print("")
print("")
#Scenario 1:
#You are a programmer for a fledgling game developer. Your team leader has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

Assorted_enemy_dictionary = {
    "II enemy 1": {
        "Name": "Trumpet Man",
        "Health": 34,
        "Defense": 12,
        "Attack": 9,
        "Special": 3,
    },
    "II enemy 2": {
        "Name": "Drummer",
        "Health": 49,
        "Defense": 12,
        "Attack": 10,
        "Special": 3,
    },
    "II enemy 3": {
        "Name": "Guitar Villain",
        "Health": 28,
        "Defense": 12,
        "Attack": 13,
        "Special": 4,
    },
    "II enemy 4": {
        "Name": "Accordion Larry",
        "Health": 36,
        "Defense": 9,
        "Attack": 12,
        "Special": 3,
    },
    "II enemy 5": {
        "Name": "Piano Ivory Tickler",
        "Health": 100,
        "Defense": 20,
        "Attack": 50,
        "Special": 12,
    },
}

print(Assorted_enemy_dictionary)

while True:

           Enemy_Number = str(input("Which of the enemies do you wish to change?(II enemy 1, II enemy 2, II enemy 3, II enemy 4, II enemy 5?)"))
           Enemy_Stat = str(input("Which stat do you want to change?(Health, Defense, Attack, or Special?)"))
           Enemy_Stat_Change = str(input("What number should replace the previous one?(Must be a number between 1 and 100.)"))
           Assorted_enemy_dictionary[Enemy_Number].update({Enemy_Stat: Enemy_Stat_Change})
           keepgoing = input("Would you like to keep making changes?(Y/N)")
           if keepgoing != "Y":
               print("Stat(s) changed!")
               break
print(Assorted_enemy_dictionary)

print("Credit to Malachi for helping me and Raphael out")