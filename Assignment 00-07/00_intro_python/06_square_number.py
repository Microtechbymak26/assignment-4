def main ():

    number = float (input("\033[1;3m Enter a number to be squared: \033[0m"))
    number = int(number)
    print(f"\033[1;3m The square of {number} is: {number * number} \033[0m")

if __name__ == "__main__":
    main()