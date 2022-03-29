# @author Ehsan Shaghaei
# @mail   e.shaghaei@innopolis.university
# @Other  BD 09.12.1999, AAI-01 Study Group
from enum import Enum
from functools import cache
import random
from sortedcontainers import SortedDict, SortedSet
SPLITTER = '.'
BIRTH_DATE = "09.12.1999"

# Constants for interface text  
class TextConst():
    INVALID_MOVE = "Invalid Move!\n"
    FACE_COMMAND = "$$$$\tCurrent Position={}\t$$$$\nPlease enter your move.\n*HINT:ENTER AN INTEGER IN RANGE[{}..{}] TO REACH [{}]\n"
    PLAYER = "User"
    COMPUTER = "Computer"
    GAME_MODE = "ENTER THE GAME MODE?\t[A]dvisor\t[S]mart\t[R]andom\n*HINT:Enter the first letter of your choice.\n"
    ADVICE_MOVE = ">COMPUTER ADVICE={}\n"
    EXIT = "\t |><|...Exiting Game...|><|"
    ADVICE_MODE = "ADVICE MODE WERE CHOSE!\n"
    SMART_MDOE = "SMART MODE WERE CHOSE!\n"
    RANDOM_MODE = "RANDOM MODE WERE CHOSE!\n"
    MOVE=":{}--[+{}]->{}"
    WINS="{} WINS!"

# Constants for log file  
class LogConst():
    GAME_MODE = "gameMode"
    ADVICE = "advice"
    SMART = "smart"
    RANDOM = "random"
    PLAYER = "player"
    MOVES = "moves"
    COMPUTER_NAME = "computer"
    USER_NAME = "user"
    WINNER="winner"


class FPG:
    def __init__(self, dd: int, mm: int, yyyy: int):
        # initializing the values
        self.year = yyyy
        self.month = mm
        self.day = dd
        # The game initiatives according to the lecture and the examination document
        self.positions = SortedSet(range(1, dd+mm+yyyy+1))
        self.moves = SortedSet(range(1, dd+mm+1))
        self.finalPosition = dd+mm+yyyy

        # Initiallizing Variables feild
        # to store positions which can

        # positions which will lead to win of the player against us
        self.winningPositions = SortedSet()
        # positions which will lead to loose of the player against us
        self.losingPositions = SortedSet()
        # moves which will lead to our win
        self.winningMoves = SortedDict()

        # Just the method to fill the feilds above using back induction
        self._solveGamebyBackInduction(positionOnBoard=self.finalPosition)

    # receives the position on the board of the game before the player makes any move and thus exploits the strategy.
    def _solveGamebyBackInduction(self, positionOnBoard):
        # first of all we check if the position we are using is a admissable position in our FPG
        if self.positions.__contains__(positionOnBoard):

            # if the player X wants to make a move and look at board and the other player already landed on the final position, thus the player X lost.
            # let us call it a loosing position
            if positionOnBoard == self.finalPosition:
                self.losingPositions.add(self.finalPosition)

            # now lets iterate over the moves which helped us to land on a positions to make the player against us loose.
            for move in self.moves:
                # determines if we are not checking invalid moves. specialling if we are at position 2 and check if a hop of 21 brang us here :D avoid contradiction
                if self.positions.__contains__(positionOnBoard-move):
                    # This is a memorable position:D, it helped us to win. so let's store it as a position which will lead us to win
                    self.winningPositions.add(positionOnBoard-move)
                    # Lets not forget where we came from, this was a move which helped us to make our Opponent loose
                    self.winningMoves.setdefault(
                        positionOnBoard-move, positionOnBoard)

        # well we checked only for one move, lets do the back tracking again, in otherwords let's do back-induction.
        # First lets make sure the room we gotta back track in valid positions
        if self.positions.__contains__(positionOnBoard-max(self.moves)-1):
            # Now we know since from this position we can not lead to a loosing point for our openent, thus it is another loosing point so lets mark it as a loosing point.
            self.losingPositions.add(positionOnBoard-max(self.moves)-1)
            #  Now, Let's backtrack which moves will lead to this position.
            self._solveGamebyBackInduction(positionOnBoard-max(self.moves)-1)

# ENUM for game modes
class GameMode(Enum):
    RANDOM = 1
    SMART = 2

# an advisor bot which exploits the winning positions regarding it's FPG game and mode.
class AdvisorBot:
    # initialized the Advisor object by a @object FPG and game mode
    def __init__(self, fpg: FPG, mode: GameMode):
        self.fpg = fpg
        self.mode = mode
    # makes an advice with a possible winning strategy
    def makeAdvice(self, position):
        # checks if the given position is a valid position
        if not self.fpg.positions.__contains__(position):
            raise Exception("Invalid Position "+str(position))
        # giving an advice regarding the given strategy [smart]
        if (self.mode == GameMode.SMART) and (not self.fpg.losingPositions.__contains__(position)):
            return self.fpg.winningMoves.get(position)
        # giving an advice regarding the given strategy [random]
        elif (self.mode == GameMode.RANDOM):
            return min(random.choice(self.fpg.moves)+position,myfpg.finalPosition)
        # chooses random strategie if anything went wrong.
        else:
            return min(random.choice(self.fpg.moves)+position,myfpg.finalPosition)



if __name__ == "__main__":
    log = {}

    dd, mm, yyyy = map(int, BIRTH_DATE.split(SPLITTER))

    myfpg = FPG(dd, mm, yyyy)

    advice_flag = False
    game_position = input("Choose ur initial position?Non-integer/Invalid value for random choice\n") #random.choice(myfpg.positions)
    try:
        game_position = int(game_position)
        if not myfpg.positions.__contains__(game_position):
            game_position = random.choice(myfpg.positions)
    except Exception as ex :
        game_position = random.choice(myfpg.positions)
    gameMode = GameMode.RANDOM

    try:
        # initializing the user entry commands
        cmd = ''
        # getting game mode from user and logging the game mode
        while not ((cmd == 'A') | (cmd == 'S') | (cmd == 'R')):
            cmd = input(TextConst.GAME_MODE).upper()
        if cmd == 'A':
            advice_flag = True
            gameMode = GameMode.SMART
            print(TextConst.ADVICE_MODE)
            log[LogConst.GAME_MODE] = LogConst.ADVICE
        elif cmd == 'S':
            advice_flag = False
            gameMode = GameMode.SMART
            print(TextConst.SMART_MDOE)
            log[LogConst.GAME_MODE] = LogConst.SMART
        elif cmd == 'R':
            advice_flag = False
            gameMode = GameMode.RANDOM
            print(TextConst.RANDOM_MODE)
            log[LogConst.GAME_MODE] = LogConst.RANDOM
        else:
            advice_flag = False
            gameMode = GameMode.RANDOM
            print(TextConst.RANDOM_MODE)
            log[LogConst.GAME_MODE] = LogConst.RANDOM

        # creating an instance of our AdvisorBot
        bot = AdvisorBot(myfpg, gameMode)

        # getting ready to log moves
        log[LogConst.MOVES]={}
        
        # Play the game till it's over!
        while not game_position == myfpg.finalPosition:
            # Getting the user move (printing the advice in case of request reserve) 
            cmd = input(TextConst.FACE_COMMAND.format(\
                game_position, myfpg.moves[0], myfpg.moves[-1], myfpg.finalPosition)\
                +TextConst.ADVICE_MOVE.format(bot.makeAdvice(game_position)-game_position)) if advice_flag\
                else input(TextConst.FACE_COMMAND.format(game_position, myfpg.moves[0], myfpg.moves[-1], myfpg.finalPosition))
            # Handeling Invalid Moves
            if (game_position + int(cmd)> myfpg.finalPosition) or (not myfpg.moves.__contains__(int(cmd))) :
                print(TextConst.INVALID_MOVE)
                continue
            # Finalizing the move and logging
            else: 
                print(TextConst.PLAYER+TextConst.MOVE.format(game_position,int(cmd),game_position+int(cmd)))
                log[LogConst.MOVES][str((game_position,game_position+int(cmd)))]=LogConst.PLAYER
                game_position += int(cmd)
            # Checking the winner
            if game_position == myfpg.finalPosition:
                print(TextConst.WINS.format(TextConst.PLAYER))
                log[LogConst.WINNER]=LogConst.PLAYER
                continue
            # Computer taking a move
            computer_move = bot.makeAdvice(game_position)
            # * Illigal moves are already handled in bot implemention
            print(TextConst.COMPUTER+TextConst.MOVE.format(game_position,computer_move-game_position,computer_move))
            log[LogConst.MOVES][str((game_position,computer_move))]=LogConst.COMPUTER_NAME
            game_position = computer_move
            # Checking the winner
            if game_position == myfpg.finalPosition:
                print(TextConst.WINS.format(TextConst.COMPUTER))
                log[LogConst.WINNER]=LogConst.COMPUTER_NAME
                continue
             
        with open('./game.json', 'w+') as f:
            f.write(str(log).replace('\'','\"'))
    except KeyboardInterrupt:
        print(TextConst.EXIT)
    except Exception as ex:
        print('\nERROR:'+str(ex)+TextConst.EXIT)
        raise ex
  
