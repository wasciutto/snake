from SnakeGame import SnakeGame

from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

todos = {}

class SnakeSimple(Resource):
    def get(self):
        game = SnakeGame()
        game.newGame()
        return {'turn':game.turn,'snakeLength':game.snakeLength,'validGame':game.validGame,
    'gameBoard':json.dumps(game.gameBoard)}

    def put(self):
        return "POST"

api.add_resource(SnakeSimple, "/")

if __name__ == '__main__':
    app.run(debug=True)