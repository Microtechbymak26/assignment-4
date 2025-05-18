import random

NUM_SIDES = 6

def main ():
   
   die1 = random.randint(1, NUM_SIDES)
   die2 = random.randint(1, NUM_SIDES)

   total = die1 + die2

   print(f"Die have {NUM_SIDES} sides and Die one is {die1}, Die two is {die2}, Total is {total}")

if __name__ == "__main__":
    main()