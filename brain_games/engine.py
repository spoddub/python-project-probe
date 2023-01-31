import prompt


def run(game):
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello, {}'.format(name))
	print(game.DESCRIPTION)

	for CURCLE in range(0, 3):
		question, correct_answer = game.question_and_correct_answer()
		print(f"Question: {question}")
		user_answer = prompt.string("Your answer: ")

		if not (user_answer == correct_answer):
		print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {name}!")
		break
		else:
		print("Correct!")
		CURCLE += 1
		if CURCLE == 3:
		print(f"Congratulations, {name}!")
