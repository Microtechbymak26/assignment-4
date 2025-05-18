INCHES_PER_FOOT = 12

def main ():
    feet = int(input("Enter a value for feet:"))
    inches = feet * INCHES_PER_FOOT
    print(feet, "Feet equals to",inches, "inches")

if __name__ == "__main__":
    main()