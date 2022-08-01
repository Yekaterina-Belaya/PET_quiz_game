print("Welcome to the quiz!")
print("You'll be given a country, and you'll need to name it's country.")

playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    quit()
print("Ok, let's start!")

score = 0

answer = input("What is the capital of Canada? ")
if answer.title() == "Ottawa":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Peru? ")
if answer.title() == "Lima":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Australia? ")
if answer.title() == "Canberra":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You've answered " + str(score) + " questions correctly!")