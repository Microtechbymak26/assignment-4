def main ():

    triangle_side1 = float(input("\033[1;3m Enter the length of the first side of the triangle: \033[0m"))
    triangle_side2 = float(input("\033[1;3m Enter the length of the second side of the triangle: \033[0m"))     
    triangle_side3 = float(input("\033[1;3m Enter the length of the third side of the triangle: \033[0m"))

    print(f"\033[1;3m The perimeter of the triangle is: {triangle_side1 + triangle_side2 + triangle_side3} \033[0m")


if __name__ == "__main__":
    main()