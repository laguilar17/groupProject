from flask import Flask, render_template, request, redirect, flash
from static.functions import HangmanGame

app = Flask(__name__)
app.secret_key = "my secret key"

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
    error = None

    if request.method == 'POST':
        letter = request.form['char']
        if len(letter) > 1:
            flash('Invalid Input. You have entered too many characters')
        elif gameInstance.guess(letter) == True:
            if (gameInstance.winCon() == 'play'):
                pass
            elif(gameInstance.winCon() == 'win'):
               return redirect("/win")
            else:
                return redirect("/lose")
        else:
            flash('You already guessed that letter')

    current_word = gameInstance.word_progress()
    wrong_guess = ''.join(gameInstance.wrongGuesses)
    
    rem_guesses = gameInstance.remainingGuesses()

    return render_template("game.html", word=current_word, letter=letter, wrong_guess=wrong_guess, remain_guess=rem_guesses,error=error)


@app.route('/win', methods=['GET', 'POST'])
def win():
    correct_word = gameInstance.getWord()
    gameInstance.playAgain()
    return render_template("win.html", name="YOU WON", word=correct_word)


@app.route('/lose', methods=['GET', 'POST'])
def lose():
    correct_word = gameInstance.getWord()
    gameInstance.playAgain()
    return render_template("lose.html", name='YOU LOST', word=correct_word)


if __name__ == '__main__':
    app.run()
