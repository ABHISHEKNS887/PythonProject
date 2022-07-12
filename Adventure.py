name = input("Type your name: ")
print("Welcome", name, "to the game")

answer = input("You have come to the dirt road, and it is a dead end. You need to go left or right. Which one do you "
               "choose? ").lower()

if answer == 'left':
    a2 = input("You come to a river, you can walk around it or swim across. Type walk to walk around or swim to swim "
               "across. ").lower()
    if a2 == "swim":
        print("You eaten by alligator, You lost. ")
    elif a2 == "walk":
        print("You walked miles and lost energy, You lost. ")
    else:
        print("Not a valid input, you lost")
elif answer == 'right':
    a3 = input("You come to the bridge, it looks wobbly. Do you want to cross it or go back, (cross/back): ").lower()

    if a3 == "back":
        print("you go back and lose.")
    elif a3 == "cross":
        a4 = input("you cross the bridge. you met a stranger. Do you want to talk to him,Type (yes/no)").lower()
        if a4 == "yes":
            print("You got stabbed, you lost.")
        elif a4 == 'no':
            print("you crossed him, You are safe. You won. ")
        else:
            print("You have not entered a valid option. pls play again")
else:
    print("Not a valid input, you lost")
