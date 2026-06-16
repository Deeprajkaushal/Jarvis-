from random import randint
n=randint(1,100)
a=-1
guesses=1
print("welcome to the number guessing game")
while(a!=n):
    a=int(input("enter your guess: "))
    if (a>n):
        print("guess a lower number")
        guesses=guesses+1
    elif (a<n):
        print("guess a higher number")
        guesses=guesses+1


print(f"congratulations! you guessed the number {n} in {guesses} guesses")