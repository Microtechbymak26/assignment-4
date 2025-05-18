def greet(name):
    return "Greetings " + name + "!"
	
def main():
    name : str = input("\033[1;3mWhats you Name? \033[0m")
    print(greet(name))

if __name__ == '__main__':
    main()
