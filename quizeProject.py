print("Welcome to my computer Quize")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()

print("Okay lets play :)")
score = 0
answer = input("What is CPU stands for? ").lower()
if answer == 'central processing unit':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer1 = input("What is GPU stands for? ").lower()
if answer1 == 'graphics processing unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 = input("What is python? ").lower()
if answer2 == 'programming language':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 = input("What is CV? ").lower()
if answer3 == 'compund v':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got "+ str(score) +" questions correct!")
print('You got ' + str((score/4)* 100)+ '%.')