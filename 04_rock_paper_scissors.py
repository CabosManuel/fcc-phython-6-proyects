import random


def play():
	user = input("(R): Rock\n" +
							 "(P): Paper\n" +
							 "(S): Scissors\n").lower()
	
	pc = random.choice(['r', 'p', 's'])

	if user == pc:
		return 'Tie -_-'
	
	if userWon(user, pc):
		return 'Win!!'
	
	return 'You lose :('


def userWon(user, other):
	# Return True if win user
	
	if ( (user == 'r' and other == 's')
		  or (user == 'p' and other == 'r')
			or (user == 's' and other == 'p') ):
		return True
	else:
		return False
	

print(play())