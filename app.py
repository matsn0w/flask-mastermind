from flask import Flask, render_template, request
from player import Player
from game import Game, ValidationError
from db import DB

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

    try:
        # create a new game
        game = Game(player, doubles, colors, positions)
    except ValidationError as e:
        return render_template('index.html', errors=e.args)

    # show the game screen
    return render_template('game.html', game=game)

