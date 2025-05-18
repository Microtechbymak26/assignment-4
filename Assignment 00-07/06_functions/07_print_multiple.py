def print_multiple(message: str, repeats: int):
   for i in range(repeats):
      # repeat = i + 1  
      print(message)

def main():
   message = input("\033[34mPlease enter a message to print: \033[0m")
   repeats = int(input("Enter a number of times to repeat your message: ")) 
   print_multiple(message, repeats)



if __name__ == '__main__':
    main() 
