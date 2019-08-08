import numpy as np
import random

class SnakeGame:

    boardSize = 16
    snakeBody = 1
    snakeHead = 2
    food = 3
    headEating = 4

    #Set up an empty game board
    def __init__(self):
        self.turn = 0
        self.snakeLength = 0
        self.validGame = True
        self.gameBoard = np.zeros((SnakeGame.boardSize, SnakeGame.boardSize))

    #Set up the snake in a random position
    def newGame(self):
        startX = random.randint(0, 15)
        startY = random.randint(0, 15)
        self.gameBoard.itemset((startX, startY), SnakeGame.snakeHead)
        pass

    #Print the game board to console
    def printGame(self):
        print(np.matrix(self.gameBoard))

    def checkSnakeSize(self):
        pass

    def checkSnakeEating(self):
        pass

if __name__ == "__main__":
    game = SnakeGame()
    game.newGame()
    game.printGame()