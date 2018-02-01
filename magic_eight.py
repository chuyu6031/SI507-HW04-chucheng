import random

def question():
	answer = input("What is your question?")
	return answer

answer = question()
print(answer)

def random_fortune():
	responses = [
		"It is certain!",
		"It is decidedly so",
		"Without a doubt",
		"Yes definitely",
		"You may rely on it",
		"As I see it, yes",
		"Most likely",
		"Outlook good",
		"Yes",
		"Signs point to yes",
		"Reply hazy try again",
		"Ask again later",
		"Better not tell you now",
		"Cannot predict now",
		"Concentrate and ask again",
		"Don't count on it",
		"My reply is no",
		"My sources say no",
		"Outlook not so good",
		"Very doubtful"
		]

	x = random.randint(0, 19)
	return responses[x]

def pick_answer():
	ten_answersC = ["Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again",
					"Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
	return(random.choice(ten_answersC))


response = random_fortune()
print(response)

response2 = pick_answer()
print(response2)

def check_question():
	answer = ""

	while answer != "quit":
		answer = question()
		if answer[-1] != "?":
			print("I’m sorry, I can only answer questions.")
