def main():
    mass = float(input("\033[1;3m Enter the mass in kilograms:\033[0m"))
    speed_of_light = 299792458  # speed of light in m/s
    energy = mass * speed_of_light ** 2

    print(f"The energy equivalent to {mass} kg is {energy} joules.")
if __name__ == "__main__":
    main()