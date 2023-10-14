import random


def computer_guess_number(limit):
	print("-----------")
	print("Welcome! :)")
	print("-----------")
	print(f"Select a number between 1 and {limit}")

	lower_limit = 1
	upper_limit = limit

	response = ""
	while response != "c":
		# Generate prediction
		if lower_limit != upper_limit:
			prediction = random.randint(lower_limit, upper_limit)
		else:
			prediction = lower_limit
		
		# Get user response
		response = input(f"PC: My prediction is {prediction}. \n\n" + 
				"- If is less than, send (L)\n" +
				"- If is greater than, send (G)\n" +
				"- If is correctly, send (C)\n").lower() # .lower() Lower case input
		
		if response == "g":
			upper_limit = prediction - 1 # upper_limit--
		elif response == "l":
			lower_limit = prediction + 1 # lower_limit++
	
	print(f"\nYees! the computer guess your number: {prediction}")


computer_guess_number(16)