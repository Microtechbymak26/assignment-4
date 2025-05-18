def main():

    fehrenheit = float(input("\033[1;3m Enter the temperature in Fahrenheit: \033[0m"))
    celsius = (fehrenheit - 32) * 5.0/9.0
    print(f"temperature : {fehrenheit}F = {celsius}C")

if __name__ == "__main__":
    main()