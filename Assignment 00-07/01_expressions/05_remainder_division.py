def main ():

    dividend = int(input("Enter the number to be divided:"))
    divisor = int(input("Enter the number to divide by:"))
     
    quotient = dividend // divisor
    print("The quotient is", quotient)
    remainder = dividend % divisor
    print("The remainder is", remainder)

if __name__ == "__main__":
    main()
