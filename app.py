from flask import Flask, render_template, request
from static.functions import HangmanGame

app = Flask(__name__)

global gameInstance
gameInstance = HangmanGame()
# word = game.word
# guesses = game.guesses
# wrongGuesses = game.wrongGuesses
# word_progress = game.word_progress()
# def gameInstance(gameTemp):
#     gameTemp
#
# def wordProgress(gword):
#     game.guess(gword)
#
#
# def retrieveWord():
#     return game.getWord()


def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]


@app.route('/')
def home():  # put application's code here
    details = readDetails('static/details.txt')
    return render_template("home.html", name='Group 4', aboutMe=details)
    # return render_template("home.html")


@app.route('/game', methods=['GET', 'POST'])
def game():
    # word = retrieveWord()
    # game = HangmanGame()
    # word = game.word
    # wrong_guess = None
    # gameInstance(game)
    letter = None

    if request.method == 'POST':
        letter = request.form['char']
        gameInstance.guess(letter)
        # wordProgress(letter)

    current_word = gameInstance.word_progress()
    # current_word = word_progress
    wrong_guess = ''.join(gameInstance.wrongGuesses)
    # wrong_guess = "test"

    return render_template("game.html", word=current_word, letter=letter, wrong_guess=wrong_guess)


@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    return render_template('form.html', name=name)


if __name__ == '__main__':
    app.run()
