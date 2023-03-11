import random

options = ["rock","paper","scissors"]
option_conversion = {"rock":0,"paper":1,"scissors":2}
result_conversion = {0:"tie",1:"won",2:"lost"}


def determine(user,computer):
    first = option_conversion[user]
    second = option_conversion[computer]
    relative = ( first-second )%3
    return result_conversion[relative]


while True:
    user = input("Your choice (rock/paper/scissors):")
    computer = random.choice(options)
    try:
        result = determine(user, computer)
        print(user, computer, result)
    except:
        print("Incompatible choice:",user)

    play_again = input("Play again (y?):").lower()
    if play_again != "y": break