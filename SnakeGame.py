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
        #Place the head
        #Range assures enough room for body without bounds checking
        startX = random.randint(4, SnakeGame.boardSize - 5)
        startY = random.randint(4, SnakeGame.boardSize - 5)
        self.gameBoard.itemset((startX, startY), SnakeGame.snakeHead)

        #Choose a direction to build the body
        randDirection = random.randint(0, 3)
        #Build up
        if(randDirection == 0):
            for i in range(1, 5):
                self.gameBoard.itemset((startX - i, startY), SnakeGame.snakeBody)
        #Build down
        elif(randDirection == 1):
            for i in range(1, 5):
                self.gameBoard.itemset((startX + i, startY), SnakeGame.snakeBody)
        #Build left
        elif(randDirection == 2):
            for i in range(1, 5):
                self.gameBoard.itemset((startX, startY - i), SnakeGame.snakeBody)
        #Build right
        elif(randDirection == 3):
            for i in range(1, 5):
                self.gameBoard.itemset((startX, startY + i), SnakeGame.snakeBody)

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