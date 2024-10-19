import random

n = random.randint(1, 100)
print("\t\tGuessing Game Challenge...\n")
print(
    """WELCOME TO GUESS ME!
I'm thinking of a number between 1 and 100
If your guess is more than 10 away from my number, I'll tell you you're COLD
If your guess is within 10 of my number, I'll tell you you're WARM
If your guess is farther than your most recent guess, I'll say you're getting COLDER
If your guess is closer than your most recent guess, I'll say you're getting WARMER
LET'S PLAY!"""
)

guesses = [0]
while True:
    tmp = int(input("Guess a number : "))
    if (tmp < 1) or (tmp > 100):
        print("OUT OF BOUND")
        continue
    if tmp == n:
        print(
            f"CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!")
        break
    guesses.append(tmp)
    if guesses[-2]:
        if abs(n - tmp) < abs(n - guesses[-2]):
            print("WARMER")
        else:
            print("COLDER")
    else:
        if abs(tmp - n) <= 10:
            print("WARM")
        else:
            print("COLD")
