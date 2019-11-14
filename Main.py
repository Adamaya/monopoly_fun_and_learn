import random
import PIL.Image
import time
from pygame import mixer  # Load the popular external library

number_of_players = int(input())  # number of players to be played
players_details_name = {}  # names of the players
players_details_email = {}  # email of the players
players_scores = {}  # score of the players
players_remaining_chances = {}  # number of steps remaining per player
last_game_by_player = {}  # last played game(number) by player
game_owners = {"guess_the_logo": None, "who_is_who": None, "game 3": None, "penalty": None, "game 5": None,
               "game 6": None,
               "game 7": None, "game 8": None, "game 9": None, "game 10": None, "bonus": None, "game 12": None,
               "game 13": None, "game 14": None, "game 15": None, "game 16": None, "game 17": None,
               "game 19": None, "game 20": None, "game 21": None, "game 22": None, "game 23": None, "game 24": None,
               "game 26": None, "game 27": None}  # owner(player) of the game by default None

games_name_with_codes = {1: "guess_the_logo", 2: "who_is_who", 3: "game 3", 4: "penalty", 5: "game 5", 6: "game 6",
                         7: "game 7",
                         8: "game 8", 9: "game 9", 10: "game 10", 11: "bonus", 12: "game 12", 13: "game 13",
                         14: "game 14",
                         15: "game 15", 16: "game 16", 17: "game 17", 18: "penalty", 19: "game 19", 20: "game 20",
                         21: "game 21",
                         22: "game 22", 23: "game 23", 24: "game 24", 25: "bonus", 26: "game 26",
                         27: "game 27"}  # particular game code(number)

