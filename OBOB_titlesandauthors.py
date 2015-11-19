# OBOB 2016 quiz to help with learning book title and Authors

import os
import random

library = {
	'Charlie Bumpers vs. the Teacher of the Year' : 'Bill Harley',
	'Diamond Willow' : 'Helen Frost',
	"Escape from Mr. Lemoncello's Library" : 'Chris Grabenstein',
	'Flora and Ulysses' : 'Kate DiCamillo',
	'How to Train Your Dragon' : 'Cressida Cowell',
	'The Lightning Thief' : 'Rick Riordan',
	'A Long Walk to Water' : 'Linda Sue Park',
	'Mission Unstoppable' : 'Dan Gutman',
	'Mountain Dog' : 'Margarita Engle',
	'No Talking' : 'Andrew Clements',
	'Rooftoppers' : 'Katherine Rundell',
	'The Sasquatch Escape' : 'Suzanne Selfors',
	'The Shadows' : 'Jacqueline West',
	'Shiloh' : 'Phyllis Reynolds Naylor',
	'What was Ellis Island?' : 'Patricia Brennan Demuth',
	'What was the March on Washington?' : 'Kathleen Krull'
}

def pick(m):
	"""Returns a random (key, value) pair from dictionary m"""
	return random.choice(m.items())

def game_setup():
	"""Prints menu of games; returns game selected and number of questions"""
	print '\t1 - Guess the Author\n\t2 - Guess the Title\n'
	game = int(raw_input('Which one do you want to play? (1/2) '))
	print
	number = int(raw_input('How many questions would you like? '))
	print
	return(game, number)

def games(dict, game, num):
	"""Executes game selected; counts and returns number of correct responses"""
	correct_count = 0
	for n in range(num):
		title, author = pick(dict)

		if game == 1:
			guess_author = raw_input('Who wrote "%s"? ' % title)
			if guess_author == author:
				print "That's correct!\n"
				correct_count += 1
			else:
				print 'Sorry, the correct answer is %s.\n' % author

		elif game == 2:
			guess_title = raw_input('What book did %s write? ' % author)
			if guess_title == title:
				print "That's correct!\n"
				correct_count += 1
			else:
				print 'Sorry, the correct answer is "%s".\n' % title

	return correct_count

def encouraging_message(percent_count):
	if percent_correct == 1.0:
		print 'You got all %d questions right! AWESOME!\n' % number
	elif percent_correct >= 0.9:
		print "So close to perfect -- %d out of %d correct! You're almost there!\n" % (correct_count, number)
	elif percent_correct >= 0.75:
		print "You're getting good -- you only missed %d questions! Keep it up!\n" % (number - correct_count)
	elif percent_correct >= 0.5:
		print "You got more than half right. Keep working at it!\n"
	elif percent_correct >= 0.3:
		print "Keep trying! Next time I bet you'll do better!\n"
	else:
		print "That was a tough round. Practice makes perfect!\n"

def play_again():
	"""Prompts to play again; executes game selected or exits"""
	repeat = raw_input('Would you like to play again? (y/n) ')
	print
	if repeat == 'y':
		game, number = game_setup()
		percent_correct = games(library, game, number) / float(number)
		encouraging_message(percent_correct)
		play_again()
	else:
		print "Good work. Come back soon!\n"


os.system('clear')

print 'Hello and welcome to the OBOB 2016 titles and authors quiz!\n'
name = raw_input("What's your name? ")
print
print 'Great to meet you, %s!\n' % name
print 'I have two games for you:'
game, number = game_setup()
print 'Great! Here we go!\n'

percent_correct = games(library, game, number) / float(number)

encouraging_message(percent_correct)

play_again()