import random

def question():
	answer = input("What is your question?")

def pick_answer():
	ten_answersC = ["Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again", 
					"Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
	return(random.choice(ten_answersC))