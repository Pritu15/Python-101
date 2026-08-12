import random

jackpot=random.randint(1,100)

attempt=0
guess=int(input("Guess your number: "))
attempt+=1

while guess!=jackpot:
    if guess<jackpot:
        print('Wrong!Guess higher')
    else:
        print("Wrong! Guess Lower")
    guess=int(input("Guess you number:"))
    attempt+=1
print("Correct Guess")
print("Number of attempts: ",attempt)