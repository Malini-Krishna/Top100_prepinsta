print("Welcome to my computer quiz! ")
playing=input("Do you want to play? yes/no ")

#print(playing)
#using lower helps us to ignore case sensitive here of user input
if playing.lower() != "yes":
    quit() #exits the code

print("Okay! let's play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower()=="central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower()=="graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower()=="random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("you got" +str(score) + "questions correct!")
print("you got" +str((score/3)*100) + "%!")
