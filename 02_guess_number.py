import random


# 2 lines to separation import and code (Python Style Guide)
def guess_number(max):
	print("-----------")
	print("Welcome! :)")
	print("-----------")
	print(f"Try to guess the number between 1 and {max}")

	random_number = random.randint(1, max) # Random number between {1, max}

	prediction = 0

	while prediction != random_number:
		prediction = int( input("Your number: ") ) # Convert string to int

		if prediction < random_number:
			print("Your number is less than random\n")
		elif prediction > random_number:
			print("Your number is GREATER than random\n")
	
	print(f"Congratulations! You guessed the number {random_number} correctly\n")


# 2 lines to separation function and call
guess_number(16)