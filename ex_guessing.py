import random

secret = random.randint(1,20)
print(secret)

name = input("What is your name?")
print("Well, "+name+", I am thinking of a number between 1 and 20")

for i in range(6):
    guess = int(input("Take a guess: "))
    if guess > secret:
        print("Your guess is too high.")
    elif guess < secret:
        print("Your guess is too low.")
    else:
        print("Good job "+name+"! You have guessed my number in "+str(i+1)+" tries")
        break

if i==5: #added to keep track if user entered all wrong answers
    print("Nope. The number I was thinking of was "+str(secret))
    
    

# Alternative way of using additional counter to keep track if all answers are wrong
'''
import random

secret = random.randint(1,20)
print(secret)

name = input("What is your name?")
print("Well, "+name+", I am thinking of a number between 1 and 20")


counter = 1  #added to keep track if user entered all wrong answers
for i in range(6):
    guess = int(input("Take a guess: "))
    if guess > secret:
        print("your guess is too high")
    elif guess < secret:
        print("your guess is too low")
    else:
        print("Good job. You have guessed in "+str(i+1)+" tries")
        break
    counter = counter + 1 #added to keep track if user entered all wrong answers

if counter == 7: #added to keep track if user entered all wrong answers
    print("Secret number is "+str(secret))
'''