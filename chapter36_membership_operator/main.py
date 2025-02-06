# in / not in => check whether a value/variable is in a sequence (string, list,...)

word = "HOME"
guess = input("Guess a letter: ").upper()

if guess in word:
    print(f"There is a letter {guess} in the secret word")
else:
    print(f"{guess} is not in the secret word")