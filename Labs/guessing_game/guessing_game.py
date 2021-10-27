"""A number-guessing game."""

# Put your code here
#let's make a random number selection

import random
randomizer = random.randrange(1, 100)
#print(randomizer)

#let's greet the player
name = input('Hello, what is your name? ')
welcome_message = name + ", I'm thinking of a number between 1 and 100. \n Try to guess my number."
print(welcome_message)

# Limit the number of tries a player gets:
limiter = 3

count_tries = 0
# let's create a randomized congratulation message!
congrats = ['Awesome, ', "Well done, ", "Terrific, ", "Good job, "]
random_congrats = random.choice(congrats)
#let's loop through the game
guess = input("Your guess? ")



def game_loop():
    randomizer = random.randrange(1, 100)
    print(welcome_message)
    count_tries = 0
    guess = input("Your guess? ")
    guess_as_int = int(guess)
    while randomizer != guess and count_tries < limiter:
        print("looping the game")
        count_tries += 1
        guess_as_int = int(guess)
        #if  guess is more than the value of randomizer, then
        #we should print "too high", and ask to guess again
        if guess_as_int > randomizer:
            print("Your guess is too high, try again.")
            guess = input("Your guess? ")
        #elif, print "too low"
        elif guess_as_int < randomizer:
            print("Your guess is too low, try again.")
            guess = input("Your guess? ")
        #else, we congratulate the player and stop the loop
        else:
            print(f"{random_congrats}{name}! That took you {count_tries} tries.")
            return

def game_start():
    game_loop()
    if count_tries == limiter:
        print(f"Shucks, you didn't guess it in {limiter} tries. Better luck next time, {name}.")
        restart_game = input("Do you want to play again?  (y or n)")
        if restart_game[0].lower() == "y":
            # New game
            game_loop()
        else:
            print(f"Have a nice day, {name}.")
            

game_start()
