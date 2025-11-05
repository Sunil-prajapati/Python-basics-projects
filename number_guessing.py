import random

# r = random.randrange(-5, 11)
# print(r)

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger tham 0 next time.")
        quit()
else:
    print("plase type a number next time")
    quit()
random_number = random.randint(0,top_of_range)


gusses = 0
while True:
    gusses+= 1
    user_guess = input("make aguess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("plase type a number next time")
        continue
    
    if user_guess == random_number:
        print("Ypu got it!")
        break
    elif(user_guess > random_number):
        print("you were above the number")
    else:
        print("you were below the number")
        
print("you got it in", gusses, "guesses")