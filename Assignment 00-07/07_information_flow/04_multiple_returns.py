def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address : str = input("What is your email address?: ")
    
    return first_name, last_name, email_address

def main():
    print("Received the following user data:", get_user_info())

if __name__ == "__main__":
     main()
     