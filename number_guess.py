print("Hello :)")
import random
#print(random.randrange(start,stop))
top_of_range=int(input("Type a number:"))
if top_of_range<=0:
    print("pls type a number larger than zero")
    quit()
random_number=random.randint(0,top_of_range)
print(random_number)

while True:
    user_guess = int(input("Make a guess: "))
    if user_guess == random_number:
     print("you got it!!")
     break
    else:
      print("You got it wrong!")