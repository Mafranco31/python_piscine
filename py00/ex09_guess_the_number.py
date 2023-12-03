from random import randint

num = randint(1, 99)
guess = 0
tries = 0
while (guess != num):
    guess = input("What's your guess between 1 and 99?\n>> ")
    tries += 1
    if (guess == "exit"):
        print("Goodbye!")
        exit()
    elif not guess.isdigit():
        print("That's not a number.")
        continue
    if int(guess) == num:
        break
    elif int(guess) < num:
        print("Too low!")
    elif int(guess) > num:
        print("Too high!")

if tries == 1:
    print("Congratulations! You got it on your first try!")
    if num == 42:
        print("The answer to the ultimate question of life, the universe and everything is 42.")
else:
    print(f"Congratulations, you've got it !\nYou won in {tries} attempts!")