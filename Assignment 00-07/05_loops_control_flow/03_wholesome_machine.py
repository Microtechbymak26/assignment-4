from colorama import Fore, Style


AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)
    user_feedback = input(Fore.BLUE + "" + Style.RESET_ALL) 

    while user_feedback != AFFIRMATION:  
       
        print("That was not the affirmation.")

        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input(Fore.BLUE + "" + Style.RESET_ALL)

    print("That's right! :)")

if __name__ == '__main__':
    main()
