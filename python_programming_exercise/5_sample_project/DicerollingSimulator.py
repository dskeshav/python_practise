import random

def roll(sides):
    dice_roll=random.randint(1,sides)
    return dice_roll

def main():
    sides=6
    rolling=True
    while rolling:
        roll_again=input("Ready to ROLL? Roll=Enter, Q=Quit. ")
        if roll_again.lower()!='q':
            num_rolled=roll(sides)
            print("You rolled a ", num_rolled)
        else:
            rolling=False
    
    print("Thanks for playing")
    













main()