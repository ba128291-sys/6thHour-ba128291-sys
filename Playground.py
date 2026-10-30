print("Intercom: Hello there you unfortunate soul.")
print("Intercom: Right an introduction is in order")
print("Intercom: Sadly you died and didn't make it to heaven, or hell")
print("Intercom: You are in a sad little place called a 'programmer's computer'.")
print("Intercom: I would say there's entertainment but sadly it's not for you it's for me.")
print("Intercom: In front of you are three bottles of water. Two of them are filled with laxatives.")
print("Intercom: Question remains, which one are you going to pick?")
print(" ")
print("You look at the table and see the three water bottles.")

user_input = input("Do you pick A, B, or C?: ")
if user_input == "A":
    print("You drink A and wait for a few minutes.")
    print("Intercom: You know if you drank B there is a different message... also that was laxatives.")
elif user_input == "B":
    print("You drink B and wait for a few minutes.")
    print("Intercom: YOU FOOL!!! You drank laxatives!! And there isn't a toilet in sight!! HAHAHAHAH")
    print("Game over")
else:
    print("You drink C and wait for a few minutes.")
    print("Intercom: Hmmmm, either you're extremely lucky or you cheated.")

user_input = input("If you got a game over retry, if you didn't get a Game Over input 12 and keep going: ")

print(" ")
print("Intercom: I'm worried that you will get too smart. Okay picture this.")
print("Intercom: In front of you is a lever.")
print("Intercom: Now do you want to pull the lever?")

user_input = input("Pull the lever? y/n: ")
if user_input == "y":
    print("You pull the lever.")
    print("Nothing happened.")
    print("Intercom: Ok so you pulled a lever and nothing happened.")
    print("Intercom: ...")
    print("Intercom: What are you waiting for?")
elif user_input == "n":
    print("You didn't pull the lever.")
    print("Nothing happened.")
    print("Intercom: Hmmm, you are smart. Nothing would've happened anyway and you chose not to waste your time.")
    print("Intercom: Good for you.")

print(" ")
print("Intercom: I'm bored, time for a new approach!")
print("Intercom: Alright then you are now in a maze.")
print("Intercom: Get to the end and I might consider releasing you from this digital hellscape.")
print("Intercom: If you do something stupid I will release my monsters on you.")
print("Intercom: Ok, 3, 2, 1, GO!!")
print(" ")

print("In front of you are three hallways.")
user_input = input("Do you go left, right, or straight?: ")
if user_input == "left":
    print("You go left.")
    print("Now there are two hallways.")
    user_input = input("Do you go left, or right?: ")
    if user_input == "right":
        print("You go right.")
        print("Now there are four hallways.")
        user_input = input("Do you go left, right, middle1, or middle2?: ")
        if user_input == "middle1":
            print("You go down middle1.")
            print("Now there are three hallways.")
            user_input = input("Do you go left, right, or straight?: ")
            if user_input == "left":
                print("You go left.")
                print("Now there is only one hallway.")
                user_input = input("Do you go down it? y/n: ")



