MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14


def main ():

    earth_weight: float = float(input("Enter your weight on Earth: "))

    planet: str = input("Enter a Planet: ").capitalize()
    if planet == "Mercury":
        gravity_conatant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_conatant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_conatant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_conatant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_conatant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_conatant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_conatant = NEPTUNE_GRAVITY
    else:
        print("Invalid planet name.")
        return
    
    weight_on_planet: float = earth_weight * gravity_conatant
    rounded_planetry_weight =  round(weight_on_planet, 2)

    print(f"Your weight on {planet} is {rounded_planetry_weight} ")
    
if __name__ == "__main__":
  main()