from flask import Flask, render_template, request
from static.functions import HangmanGame

app = Flask(__name__)

# global gameInstance
gameInstance = HangmanGame()


def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]


@app.route('/')
def home():
    details = readDetails('static/details.txt')
    return render_template("home.html", name='Group 4', aboutMe=details)


@app.route('/game', methods=['GET', 'POST'])
def game():
    letter = None

    if request.method == 'POST':
        letter = request.form['char']
        gameInstance.guess(letter)
        # if (gameInstance.winCon() == 'play'):
        #     pass

    current_word = gameInstance.word_progress()
    wrong_guess = ''.join(gameInstance.wrongGuesses)

    return render_template("game.html", word=current_word, letter=letter, wrong_guess=wrong_guess)


# @app.route('/form', methods=['GET', 'POST'])
# def formDemo():
#     name = None
#     if request.method == 'POST':
#         name = request.form['name']
#     return render_template('form.html', name=name)


if __name__ == '__main__':
    app.run()
