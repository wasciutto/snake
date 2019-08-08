from SnakeGame import SnakeGame

from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class SnakeSimple(Resource):
    def get(self):
        game = SnakeGame()
        game.newGame()
        
        return {'turn':game.turn,'snakeLength':game.snakeLength,'validGame':game.validGame,
    'gameBoard':json.dumps(game.gameBoard)}

    def put(self):
        game = SnakeGame()
        gameString = request.form['game']
        gameMap = json.loads(gameString)
        
        game.turn = gameMap['turn']
        game.snakeLength = gameMap['snakeLength']
        game.validGame = gameMap['validGame']
        game.gameBoard = gameMap['gameBoard']
        
        game.checkSnakeSize()
        game.checkEating()
        
        return {'turn':game.turn,'snakeLength':game.snakeLength,'validGame':game.validGame,
    'gameBoard':json.dumps(game.gameBoard)}

api.add_resource(SnakeSimple, "/")

if __name__ == '__main__':
    app.run(debug=True)