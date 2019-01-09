'''
A program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

-If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
-On a player's first turn, if their guess is
	within 10 of the number, return "WARM!"
	further than 10 away from the number, return "COLD!"
-On all subsequent turns, if a guess is
	closer to the number than the previous guess return "WARMER!"
	farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''

from random import randint

random_number = randint(1,100)
#print("Ramdom number: {}".format(random_number))

while True:
	num = int(input("Guess any number from 1 to 100: "))
	if(num<1 or num>100):
		print("OUT OF BOUND")
		continue
	else:
		break


guessed_nums_list = []
guessed_nums_list.append(abs(random_number-num))

guessed = False

while not(guessed == True):
	if(guessed_nums_list[-1] == 0):
		guessed = True
	elif(1<=guessed_nums_list[-1]<=10): 
		print("WARM")
		break
	else:
		print("COLD")
		break

if(guessed == False):
	while not(guessed == True):
		num_again = int(input("Enter a closer number: "))
		guessed_nums_list.append(abs(random_number - num_again))
		if(guessed_nums_list[-1] == 0):
			guessed = True
		elif(guessed_nums_list[-1] < guessed_nums_list[-2]):
			print("WARMER")
			continue
		elif(guessed_nums_list[-1] > guessed_nums_list[-2]):
			print("COLDER")
			continue

print("You've guessed the correct number in {} tries".format(len(guessed_nums_list)))
