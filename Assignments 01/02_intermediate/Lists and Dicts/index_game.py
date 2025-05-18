
def access_element(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range"
    return lst[index]

# Function to modify an element in a list
# This function takes a list, an index, and a new value, and modifies the element at the given index.
def modify_element(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index out of range"
    lst[index] = new_value
    return lst

# Function to slice a list
# This function takes a list and two indices, and returns the sliced portion of the list.
def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start > end:
        return "Invalid slice indices"
    return lst[start:end]

# This is a simple game where the user can access, modify, or slice a list.
def main():
    my_list = ["apple", "banana", "cherry", "date", "mango"]

    while True:
        print("\nCurrent List:", my_list)
        print("Choose operation: access / modify / slice / quit")
        choice = input("Your choice: ")

        if choice == "access" or choice == "a":
            idx = int(input("Enter index to access: "))
            print("Result:", access_element(my_list, idx))

        elif choice == "modify" or choice == "m":
            idx = int(input("Enter index to modify: "))
            val = input("Enter new value: ")
            print("Updated List:", modify_element(my_list, idx, val))

        elif choice == "slice" or choice == "s":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(my_list, start, end))

        elif choice == "quit" or choice == "q":
            print("Game over. Bye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
