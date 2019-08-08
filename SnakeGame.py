import numpy as np

class SnakeGame:

    boardSize = 16

    def __init__(self):
        self.turn = 0
        self.snakeLength = 0
        self.validGame = True
        self.gameBoard = np.zeros((SnakeGame.boardSize, SnakeGame.boardSize))

    def newGame(self):
        pass

    def printGame(self):
        print(np.matrix(self.gameBoard))


if __name__ == "__main__":
    game = SnakeGame()
    game.newGame()
    game.printGame()