from player import Player
from game import Game
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    player = Player('henk')
    game = Game(player)

    return render_template('hello_world.html')
