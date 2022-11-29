import random

class HangmanGame:
    def __init__(self):
        self.word = HangmanGame.randWord()  # stores word
        self.guesses = []  # stores correct guesses
        self.wrongGuesses = []  # stores wrong guesses
        self.numGuess = 0
    

    def getWord(self):
        return self.word

    def guess(self, userInput):
        userInput = userInput.lower()

        if userInput in self.wrongGuesses:
            return False

        elif userInput in self.guesses:
            return False

        elif userInput in self.word:
            self.guesses.append(userInput)
            return True

        else:
            self.wrongGuesses.append(userInput)
            self.numGuess += 1
            return True

    def word_progress(self):
        current_word = []
        current_string = ""
        j = 0
        for i in range(len(self.word)):
            current_word.append("-")

        for x in self.word:
            for y in self.guesses:
                if x == y:
                    current_word[j] = x
            j += 1

        return current_string.join(current_word)

    def winCon(self):
        if self.word_progress() == self.word:
            return "win"
        elif self.numGuess >= 7:
            return "lose"
        else:
            return "play"

    def playAgain(self):
        self.word = HangmanGame.randWord()  # stores word
        self.guesses = []  # stores correct guesses
        self.wrongGuesses = []  # stores wrong guesses
        self.numGuess = 0

    def randWord():
        with open("static/dictionary.txt") as file:
            lines = [line.rstrip() for line in file]

        randNum = random.randint(0,len(lines))
        return lines[randNum]

    def remainingGuesses(self):
        return 7 - self.numGuess

# game = HangmanGame()
# print(game.word)
# print(game.guesses)
# print(game.wrongGuesses)
# print(game.numGuess)
#
# print("Guess h")
# game.guess('h')
# print(game.word_progress())
# print(game.guesses)
# print(game.wrongGuesses)
# print(game.numGuess)
#
# print("Guess l")
# game.guess('l')
# print(game.word_progress())
# print(game.guesses)
# print(game.wrongGuesses)
# print(game.numGuess)
#
# print("Guess a")
# game.guess('a')
# print(game.word_progress())
# print(game.guesses)
# print(game.wrongGuesses)
# print(game.numGuess)
