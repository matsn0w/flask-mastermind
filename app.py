from flask import Flask, render_template, request
from werkzeug.utils import redirect
from db import DB
from game import Game, ValidationError
from player import Player
from color import Color
from datetime import timezone, datetime

app = Flask(__name__)
database = DB('mastermind.db')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def start_game():
    # extract form data
    print(request.form)
    player = Player(request.form['player_name'])
    doubles = True if request.form['use_doubles'] == 'yes' else False
    cheats = True if request.form['use_cheats'] == 'yes' else False
    colors = int(request.form['amount_colors'])
    positions = int(request.form['amount_positions'])
    global game

    try:
        # create a new game
        game = Game(player, doubles, cheats, colors, positions)
    except ValidationError as e:
        return render_template('index.html', errors=e.args)

    # try: 
    #     database.saveGame(player, int(datetime.now(tz=timezone.utc).timestamp())  , 0)

    # show the game screen
    return render_template('game.html', game=game, colors=Color)

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
        return redirect('/win')

    return render_template('game.html', game=game, colors=Color)

@app.route('/win')
def win():
    colors = []

    for c in game.code:
        colors.append(Color(c).name)

    code = ', '.join(colors)

    return render_template('win.html', game=game, code=code)
