import random
def rps():
	user = input('Enter a choice: R for Rock, P for Paper, and S for Scissors\n')
	comp = random.choice(['R','P','S'])
	print("The computer's choice is ",comp)
	if(user==comp):
		return "It is a Tie."
	#R>S, P>R, S>P
	elif((user=='R' and comp=='S') or (user=='P' and comp=='R') or (user=='S' and comp=='P')):
		return "You Win!!!!"
	return "You Lost :-("
print(rps())