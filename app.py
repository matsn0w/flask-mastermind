from color import Color
from flask import Flask, render_template, request
from player import Player
from game import Game, ValidationError
from db import DB
from datetime import timezone, datetime

app = Flask(__name__)
database = DB('mastermind.db')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def start_game():
    # extract form data
    player = Player(request.form['player_name'])
    doubles = True if request.form['use_doubles'] == 'on' else False
    colors = int(request.form['amount_colors'])
    positions = int(request.form['amount_positions'])
    global game

    try:
        # create a new game
        game = Game(player, doubles, colors, positions)
    except ValidationError as e:
        return render_template('index.html', errors=e.args)

    # try: 
    #     database.saveGame(player, int(datetime.now(tz=timezone.utc).timestamp())  , 0)

    # show the game screen
    return render_template('game.html', game=game, colors=Color, maxcolors=colors, positions=positions)

@app.route('/game', methods=['POST'])
def guess():
    guesses = []

    # extract form data
    data = request.form.items()

    for key, value in data:
        # add int value to guesses array
        guesses.append(int(value))

    # make the guess
    result = game.guess(guesses)

    # return render_template('game.html', game=game, colors=Color, maxcolors=colors, positions=positions)
