import random

title = "welcome to the number guessing game!".title()
separator = "*" * 48

print(separator)
print(f"*{title.center(46)}*")
print(separator)

user_win = False
winning_number = random.randint(1, 100)
attempts = 0

while not user_win:
    try:
        attempts += 1
        user_number = int(input("🤖 Please, digit a number between 1 and 100: "))

        if (user_number == winning_number):
            print("🥳 Congratulations! You win!")
            print("🔁 Attempts:", attempts)
        else:
            
    except ValueError:
        print("❌ Wrong input! Please, try again.")