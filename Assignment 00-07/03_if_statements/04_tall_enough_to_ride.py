MINIMUM_HEIGHT : int = 50 

def main():
    height = float(input("\033[34m How tall are you? (in cm): \033[0m"))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
if __name__ == '__main__':
    main()