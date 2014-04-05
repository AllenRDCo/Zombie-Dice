#!/usr/bin/python

import random

# define the dice and their sides (nested dictionaries for memory optimization)
dies = {"gdie": {0: "brain", 1: "brain", 2: "brain", 3: "shotgun", 4: "feet", 5: "feet"}, "ydie": {0: "brain", 1: "brain", 2: "shotgun", 3: "shotgun", 4: "feet", 5: "feet"}, "rdie": {0: "brain", 1: "shotgun", 2: "shotgun", 3: "shotgun", 4: "feet", 5: "feet"}}


#pick die color
def pick_color():
	color = random.randrange(13)
	
	if color < 6:
		return "green"
	elif color >= 6 and color < 10:
		return "yellow"
	elif color >= 10 and color < 13:
		return "red"

#pick die side
def pick_side():
	side = random.randrange(6)
	return side

#roll the die
def roll_die():
	die = pick_color()
	side = pick_side()
	if die == "green":
		return (die, dies["gdie"][side])
	elif die == "yellow":
		return (die, dies["ydie"][side])
	elif die == "red":
		return (die, dies["ydie"][side])

#track the rolls
hit_count = 0
brain_count = 0

#take a turn and roll 3 dice
def turn():
	global hit_count
	global brain_count
	n = 0
	while n < 3:
		die_color, result = roll_die()
		if result == "brain":
			brain_count += 1
		elif result == "shotgun":
			hit_count += 1
		
		print "Rolled %s and got %s" % (die_color, result)
		n +=1
	print "Brains: %s Hits: %s" % (brain_count, hit_count)

#game starts here
print "It's zombie time!!!"
print "You want to get as many brains as possible in a turn before you get shot 3 times."
print "If you get feet that means your victim ran away, shotgun means you were shot, and brains means you devoured your victims brains!"
print
print
print "Let's go!"
#accept input from player to determine readiness, then enter a loop while hits are less than three, or if player decides to stop
play = str.lower(raw_input("Are you ready to start? y or n: "))

while play not in "yn":
	print "Sorry, response must be a 'y' or 'n'"
	play = str.lower(raw_input("Are you ready to start? y or n: "))
else:
	if play == "n":
		print "Ok, thanks for playing!"

	while play == "y":
		if hit_count < 3:
			turn()
			if hit_count < 3:	
				play = str.lower(raw_input("Do you want to roll again? y or n: "))
				while play not in "yn":
        				print "Sorry, response must be a 'y' or 'n'"
					play = str.lower(raw_input("Are you ready to start? y or n: "))
				else:
					print "Carry on!"
			else:
				print "You've been hit 3 times! Your turn is over!"
	                	play = "n"
        	        	break

