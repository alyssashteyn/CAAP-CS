# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard

moves = 0
name =  ''
lives = 3
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
    global name
    global moves
    global leaderboard #score = Score(name, moves)
    print("\n Game over!")


    if won:
        print(moves, "moves")
        print("name", name)
        score = Score(name, moves)
        if leaderboard.update(score):
            leaderboard.insert(score)
    else:
        moves = 0
        name = ""
    leaderboard.print_board()

    #if won:
    #leaderboard.update(score)
    #else:
        #current_scene = scene_map(checkpoint) #self.checkpoint checkpoint = scene_map.doorway()
    #
    # name = ''
    # moves = 0
    # lives = 3 #new
    #leaderboard.print_board()
#game_over()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
    while True:
        global name
        global moves
        print (" Let's say you're going out with a Russian girl.\n Over the span of some years, you two have gotten pretty serious.\n Your Russian princess decides it's time for you to meet her family.\n So, you two go over to her mom's house for dinner.To quit enter 'quit' at any time.\n The score operates as it does in golf. You want the least amount of points.\n Each time you advance and each time you die will result in an extra point.\n The lower the score the closer you are to acceptance/tolerance from the Russian girl's mother.\n Good luck!")
        name = input("\nLet's play. Enter your name. > ")
        if (name == 'quit'):
            exit(1)
        a_map = Map("doorway") ##raise ValueError ('todo')
        a_game = Engine(a_map)  #a_game = Engine(Map(doorway))
        moves = a_game.play()
        game_over(a_game.won())

        #print(Leaderboard.print_board())
        #game_over(a_game.won())
play_game()


#update function for leadership board
#leaderboard.print_board()
