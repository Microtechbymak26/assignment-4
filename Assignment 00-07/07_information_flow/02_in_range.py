def in_range(n, low, high): 
    if low <= n <= high:
        return True
    return False
def main():
    
    print(in_range(5, 1, 10))  
    print(in_range(0, 1, 10))  
    print(in_range(15, 1, 10)) 


if __name__ == '__main__':
    main()
