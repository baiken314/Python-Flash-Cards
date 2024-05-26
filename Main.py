from random import randint
import os
import time

state = "menu"
frontList = []
backList = []

fileName = input("Type in name of file you want to use: ")

file = open(fileName, "r")
loadString = file.read()
file.close()

if loadString != "":
	word = ""
	onFront = True
	for i in range(len(loadString)):
		if loadString[i] != ":" and loadString[i] != "|":
			word += loadString[i]
		elif loadString[i] == ":":
			if onFront:
				frontList.append(word)
				word = ""
			else:
				backList.append(word)
				word = ""
		else:
			onFront = False

print("Welcome to my flashcard program!")

while True:
	if state == "menu":
		os.system("cls")
		print("Type C to make new cards")
		print("Type S to study existing cards")
		print("Type E to edit cards")
		print("Type X to save cards")
		print("Type Q to quit")

		action = input("Enter action: ")
		if action == "C" or action == "c":
			state = "input"
		elif action == "S" or action == "s":
			state = "study"
		elif action == "Q" or action == "q":
			exit()
		elif action == "X" or action == "x":
			state = "save"
		else:
			print("Sorry, that action was not understood.")

	if state == "input":
		frontText = input("Front: ")
		if frontText == "Q" or frontText == "q":
			state = "menu"
		if state == "input":
			backText = input("Back:  ")
			
			frontList.append(frontText)
			backList.append(backText)

			print("")

	if state == "study":
		os.system("cls")

		correctIndex = randint(0, len(frontList) - 1)
		correctCard = frontList[correctIndex]
		correctChoice = randint(0, 3)
		choices = [0, 0, 0, 0]

		choice1, choice2, choice3 = 0, 0, 0
		card1, card2, card3 = 0, 0, 0

		while choice1 == choice2 or choice1 == choice3 or choice1 == correctChoice or choice2 == choice3 or choice2 == correctChoice or choice3 == correctChoice:
			choice1 = randint(0, 3)
			choice2 = randint(0, 3)
			choice3 = randint(0, 3)
		while card1 == card2 or card1 == card3 or card1 == correctIndex or card2 == card3 or card2 == correctIndex or card3 == correctIndex:
			card1 = randint(0, len(backList) - 1)
			card2 = randint(0, len(backList) - 1)
			card3 = randint(0, len(backList) - 1)

		choices[choice1] = backList[card1]
		choices[choice2] = backList[card2]
		choices[choice3] = backList[card3]
		choices[correctChoice] = backList[correctIndex]

		print(correctCard)
		print("")
		print(" 1 ", choices[0])
		print(" 2 ", choices[1])
		print(" 3 ", choices[2])
		print(" 4 ", choices[3])
		print("")

		answer = 0
		while answer <= 0 or answer >= 5:
			answer = str(input("Answer: "))

			if answer == "Q" or answer == "q":
				state = "menu"
				answer = 0
				break

			answer = int(answer)

		answer = int(answer)
		answer -= 1
		if answer > -1:
			if choices[answer] != backList[correctIndex]:
				print(backList[correctIndex])
				time.sleep(2)

	if state == "save":
		saveString = ""
		for word in frontList:
			saveString += word
			saveString += ":"
		saveString += "|"
		for word in backList:
			saveString += word
			saveString += ":"

		file = open(fileName, "w")
		file.write(saveString)
		file.close()

		state = "menu"