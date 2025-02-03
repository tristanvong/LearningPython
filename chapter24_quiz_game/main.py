questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest egg?: ",
             "How many bones are in the human body?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. 206", "B. 207", "C. 208", "D. 209"))

answers = ("C", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"The right answer was {answers[question_num]} you chose {guess}")
    question_num += 1
    print()

print("--- Results ---")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your total score is: {score}%")