

from enum import Enum
import datetime
import random

"""Constants"""
PLAYER = 'X'
COMPUTER = 'O'
EMPTY = '_'
BOARD_SIZE = 5
NUMBER_OF_PLAYERS = 1
SEARCH_TIME = 5

"""exception class, in case the user entered a none empty position"""

class NoneEmptyPosition(Exception):
    pass


"""exception class, in case the user entered number higher the board positions"""


class OutOfRange(Exception):
    pass

""" enum for game state"""

class GameState(Enum):
    tie = 'Tie'
    notEnd = 'notEnd'
    o = 'O' 
    x = 'X' 




class Board:


    def __init__(self, size):
        self.mSize = size
        self.mBoard = [[EMPTY for x in range(size)] for y in range(size)]
        self.lastMove = None

    def print(self):
        for i in range(self.mSize):
            for j in range(self.mSize):
                if j < self.mSize-1:
                    print(self.mBoard[i][j], end='|')
                else:
                    print(self.mBoard[i][j], end='')
            print()


    def getBoardPosition(self,position):
        column = position%self.mSize
        row = position//self.mSize
        return row, column

    def getLastMove(self):
        return self.lastMove

    def getRow(self, numberOfRow):
        return self.mBoard[numberOfRow]

    def getColumn(self, numberOFColumn):
        return [row[numberOFColumn] for row in self.mBoard]

    def getDiagonal(self):
        diagonal1 = [self.mBoard[i][i] for i in range(self.mSize)]
        diagonal2 = []
        j = 0
        for i in reversed(range(self.mSize)):
            diagonal2.append(self.mBoard[i][j])
            j += 1
        return diagonal1, diagonal2

    def getMainDiagonal(self):
        return [self.mBoard[i][i] for i in range(self.mSize)]

    def getSecondaryDiagonal(self):
        diagonal = []
        j = 0;
        for i in reversed(range(self.mSize)):
            diagonal.append(self.mBoard[i][j])
            j += 1
        return diagonal

    def checkIfOnMainDiagonal(self, position):
        return position % (self.mSize + 1) == 0

    def checkIfOnSecondaryDiagonal(self, position):
        return position % (self.mSize - 1) == 0

    def drawX(self, position):
        self.lastMove = position
        (row, column) = self.getBoardPosition(position)
        self.mBoard[row][column] = PLAYER

    def drawEmpty(self, position):
        (row, column) = self.getBoardPosition(position)
        self.mBoard[row][column] = EMPTY

    def drawO(self, position):
        self.lastMove = position
        (row, column) =  self.getBoardPosition(position)
        self.mBoard[row][column] = COMPUTER

    """this function gets position and checking if it empty"""
    def checkIfRubricEmpty(self, position):
        (row, column) = self.getBoardPosition(position)
        return self.mBoard[row][column] == EMPTY

    def all_same(self, listToBeChecked, char):
        return all(x == char for x in listToBeChecked)




class Game:


    def __init__(self, numberOfPlayers, boardSize):
        self.mBoard = Board(boardSize)
        self.mBoardSize = boardSize
        self.mNumberOfPlayers = numberOfPlayers
        self.mNamesList = [' ']*numberOfPlayers
        self.mTurn = None
        self.mComputerFirstPosition = None
        self.coinFlip()
        self.mBestMove = 0



    def coinFlip(self):
        turn = random.choice(['computer', 'player'])
        if turn == 'computer':
            self.mComputerFirstPosition = random.randrange(self.mBoard.mSize ** 2)
            self.mTurn = 1
        else:
            self.mTurn = 0

    def getPlayersNames(self):
        counter = 1
        while counter <= self.mNumberOfPlayers:
            try:
                playerName = input('please enter the name of player' + str(counter))
                if not playerName:
                    raise ValueError("field cannot be empty, please enter name")
                if not playerName.isalpha():
                    raise ValueError("only letters are allowed")
                if playerName in self.mNamesList:
                    raise ValueError("name already chosen please choose different name")

                self.mNamesList[counter - 1] = playerName
                counter += 1
            except ValueError as e:
                print(e)
            except Exception:
                print("unknown error")


    def getPlayerMove(self):
        while True:
            try:
                playerMove = int(input(self.mNamesList[self.mTurn] + ' please select rubric'))
                if not (0 <= playerMove <= (self.mBoardSize ** 2 - 1)):
                    raise OutOfRange("Wrong position, please choose position 0 - " + str(self.mBoardSize ** 2 - 1))

                if not self.mBoard.checkIfRubricEmpty(playerMove):
                    raise NoneEmptyPosition("this rubric taken please choose other rubric")

                return playerMove

            except (OutOfRange, NoneEmptyPosition) as e:
                print(e)
            except ValueError as e:
                print("only numbers are allowed")
            except Exception:
                print("unknown error")


    def checkForWin(self, turn):
        char = ''
        if turn % 2 == 0:
            char = 'X'
        else:
            char = 'O'
        lastMove = self.mBoard.getLastMove()
        row, col = self.mBoard.getBoardPosition(lastMove)

        if self.mBoard.all_same(self.mBoard.getRow(row), char) or \
                self.mBoard.all_same(self.mBoard.getColumn(col), char):
            return True

        if self.mBoard.checkIfOnMainDiagonal(lastMove):
            if self.mBoard.all_same(self.mBoard.getMainDiagonal(), char):
                return True

        if self.mBoard.checkIfOnSecondaryDiagonal(lastMove):
            if self.mBoard.all_same(self.mBoard.getSecondaryDiagonal(), char):
                return True

        return False

    def checkForTie(self):
        for i in range(self.mBoard.mSize ** 2):
            if self.mBoard.checkIfRubricEmpty(i):
                return False
        return True

    def genrate(self):
        possibleMoves = []
        for i in range(self.mBoard.mSize ** 2):
            if self.mBoard.checkIfRubricEmpty(i):
                possibleMoves.append(i)
        return possibleMoves

    def checkGameState(self):
        if self.checkForWin(0):
            return GameState.x

        if self.checkForWin(1):
            return GameState.o

        if self.checkForTie():
            return GameState.tie

        return GameState.notEnd


    def start(self):
        self.getPlayersNames()
        while True:
            self.mBoard.print()
            self.mTurn %= 2
            if self.mTurn % 2 == 0:
                playerMove = self.getPlayerMove()
                self.mBoard.drawX(playerMove)
            else:
                print('computer please select rubric')
                if self.mComputerFirstPosition is not None:
                    computerMove = self.mComputerFirstPosition
                    self.mComputerFirstPosition = None
                else:
                    computerMove = self.iterativeDeepSearch()

                self.mBoard.drawO(computerMove)

            gameResult = self.checkGameState()
            if gameResult.value != 'notEnd':
                self.mBoard.print()
                if gameResult.value == 'Tie':
                    print('The game is tie')
                else:
                    if self.mTurn % 2 == 0:
                        print(self.mNamesList[self.mTurn] + 'is the winner!')
                    else:
                        print('computer is the winner!')
                break

            self.mTurn += 1


    def minmax2(self, depth, isMax, alpha, beta, startTime, timeLimit):

        moves = self.genrate()
        score = self.evaluate()
        position = None

        if datetime.datetime.now() - startTime >= timeLimit:
            self.mTimePassed = True

        if not moves or depth == 0 or self.mTimePassed:
            gameResult = self.checkGameState()
            if gameResult.value == 'X':
                return -10**(self.mBoard.mSize+1), position
            elif gameResult.value == 'O':
                return 10**(self.mBoard.mSize+1), position
            elif gameResult.value == 'Tie':
                return 0, position

            return score, position

        if isMax:
            for i in moves:
                    self.mBoard.drawO(i)
                    score, dummy = self.minmax2(depth-1, not isMax, alpha, beta, startTime, timeLimit)
                    if score > alpha:
                        alpha = score
                        position = i
                        self.mBestMove = i

                    self.mBoard.drawEmpty(i)
                    if beta <= alpha:
                        break

            return alpha, position
        else:
            for i in moves:
                self.mBoard.drawX(i)
                score, dummy = self.minmax2(depth-1, not isMax, alpha, beta, startTime, timeLimit)
                if score < beta:
                    beta = score
                    position = i
                    self.mBestMove = i
                self.mBoard.drawEmpty(i)
                if alpha >= beta:
                    break

            return beta, position

    def iterativeDeepSearch(self):
        startTime = datetime.datetime.now()
        endTime = startTime + datetime.timedelta(0, SEARCH_TIME)
        depth = 1
        position = None
        self.mTimePassed = False
        while True:
            currentTime = datetime.datetime.now()
            if currentTime >= endTime:
                break
            best, position = self.minmax2(depth, True, -10000000, 10000000, currentTime, endTime-currentTime)
            depth += 1

        if position is None:
            position = self.mBestMove

        return position

    """this function gets a board line and calculate how many
        'X', 'O' and empty rubrics"""
    def calculateLine(self, line):
        oSum = line.count(COMPUTER)
        xSum = line.count(PLAYER)
        EmptySum = line.count(EMPTY)
        return oSum, xSum, EmptySum

    """this function gets a board line and calculate it score"""
    def getScoreLine(self, line):
        score = 0
        oSum, xSum, EmptySum = self.calculateLine(line)
        if xSum == 0 and oSum != 0:
            if oSum == self.mBoard.mSize:
                score += 11 ** (oSum - 1)
            score += 10 ** (oSum - 1)
        if oSum == 0 and xSum != 0:
            score += -(10 ** (xSum - 1))
        return score

    """this function evaluate the game board and return the score"""
    def evaluate(self):
        score = 0
        for i in range(self.mBoard.mSize):
            score += self.getScoreLine(self.mBoard.getRow(i))
            score += self.getScoreLine(self.mBoard.getColumn(i))

        diagonals = self.mBoard.getDiagonal()
        for i in range(2):
            score += self.getScoreLine(diagonals[i])
        return score


game = Game(NUMBER_OF_PLAYERS, BOARD_SIZE)
game.start()




