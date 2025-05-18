def subtract_seven(num):
	num = num - 7
	return num

def main():
	num: int = 7
	print("this should be zero: ", subtract_seven(num))
	
if __name__ == '__main__':
    main()