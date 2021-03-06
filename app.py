from datetime import datetime, timezone

from flask import Flask, render_template, request
from werkzeug.utils import redirect

from db import DB
from errors.validationerror import ValidationError
from models.color import Color
from models.game import Game
from models.player import Player

app = Flask(__name__)
database = DB('mastermind.db')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def start_game():
    # extract form data
    doubles = True if request.form['use_doubles'] == 'yes' else False
    cheats = True if request.form['use_cheats'] == 'yes' else False
    colors = int(request.form['amount_colors'])
    positions = int(request.form['amount_positions'])
    global game

    try:
        # create a new player and game
        player = Player(request.form['player_name'])
        game = Game(player, doubles, cheats, colors, positions)
    except ValidationError as e:
        return render_template('index.html', errors=e.args)

    # show the game screen
    return render_template('game.html', game=game, colors=Color, guesses=[])

@app.route('/stats', methods=['GET'])
def get_name():
    return render_template('name_form.html')

@app.route('/stats', methods=['POST'])
def show_statistics():
    name = request.form['player_name']
    stats = database.getStatisticsByName(name)
    return render_template('stats.html', stats=stats, name=name)

@app.route('/game', methods=['POST'])
def guess():
    guesses = []

    # extract form data
    data = request.form.items()

    for key, value in data:
        # add int value to guesses array
        guesses.append(int(value))

    # make the guess
    game.guess(guesses)

    # check if the player won
    if game.win():
        database.saveGame(game.player, int(datetime.now(tz=timezone.utc).timestamp()), game.turns, game.cheats)
        return redirect('/win')

    return render_template('game.html', game=game, colors=Color, guesses=guesses)

@app.route('/win')
def win():
    colors = []

    for c in game.code:
        colors.append(Color(c).name)

    code = ', '.join(colors)

    return render_template('win.html', game=game, code=code)
