print("Welcome to computer quiz")

playing = input("Do you want to play? ")

print(playing)

if playing.lower() != "yes":
    quit()

print("OKay! let's play:)")
score = 0

answer = input("whats does cpu stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("whats does gpu stand for? ").lower()
if answer == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/2) * 100) + " %.")
