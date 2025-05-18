import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # This is the only number left

        feedback = input(f"is {guess} too high (H) ,too low (L), or correct (C)???").lower()
    
        if feedback == "h" or feedback == "H":
            high = guess - 1
        elif feedback == "l" or feedback == "L":
            low = guess + 1
    # if feedback == "c" or feedback == "C":
    #     # The computer guessed the number correctly
    #     # print(f"yay! the computer guessed your number, {guess}, correctly!")
    #     pass        
    print(f"yay! the computer guessed your number, {guess}, correctly!")

computer_guess(10)


