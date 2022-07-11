import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please print the number which is greater than zero.")
        quit()
else:
    print("Please print the number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesess = 0
while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess > top_of_range:
            print("please type a number below", top_of_range)
            continue
    else:
        print("Type a number next time")
        continue

    guesess += 1
    if user_guess == random_number:
        print("Yes you got it!")
        break
    elif user_guess > random_number:
        print("your guess is above the number")
    else:
        print("your guess is below the number")

print("you have tries", guesess, "times.")