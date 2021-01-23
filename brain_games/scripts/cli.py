from prompt import string
def welcome_user():
	name = string('May I have your name? ')
	print('Hello, {}'.format(name))