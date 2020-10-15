import random

randNum = random.randint(1,50)
print("Welcome to Guess the number game !!")
print(randNum)
userNum = int(input("Enter your number"))
while True:
    if (randNum == userNum):
        print("Congratulation you won !!")
        break
    elif (randNum > userNum):
        print("Opps ...Your number is less.. Please Guess again ")
        userNum = int(input("Enter your number"))
    elif (randNum < userNum):
        print("Opps ...Your number is Grater.. Please Guess again ")
        userNum = int(input("Enter your number"))