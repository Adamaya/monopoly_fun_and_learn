'''
Author: Adamaya Sharma
last Modified: 14/11/2019
Version: 1.0
'''

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

# setting score equals to zero
for _ in range(1, number_of_players + 1):
    players_scores[_] = 0

# setting last game value of each player equal to zero
for _ in range(1, number_of_players + 1):
    last_game_by_player[_] = 0

# remaining chances
for _ in range(1, number_of_players + 1):
    players_remaining_chances[_] = 27

# player details input
for _ in range(1, number_of_players + 1):
    players_details_name[_] = input("Enter Player " + str(_) + " Name: ")
    # players_details_email[_] = input("Enter Player " + str(_) + " Email")


# game chooser function created
def game_chooser(game_number):
    if game_number == 1:
        print("Game " + str(game_number) + ": Guess the Logo")
        questions = ['connectivity.jpg', 'microsoft.png']
        random_number = random.randint(0, 1)
        image = PIL.Image.open(
            "C:/Users/ADAMAYA SHARMA/PycharmProjects/monoply_fun_and_learn/Logo/" + questions[random_number])
        image.show()
        print("Answer: Image number " + str(random_number))
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        if response.lower() == "y":
            return True
        elif response.lower() == "n":
            return False

    if game_number == 2:
        print("Game " + str(game_number) + ": Guess the Music")
        questions = ['Cool and Inspiring Background Music.mp3', 'Cool and Inspiring Background Music.mp3']
        random_number = random.randint(0, 1)
        mixer.init()
        mixer.music.load(questions[random_number])
        print("playing song " + str(random_number))
        mixer.music.play()
        time.sleep(30)
        mixer.music.stop()

        response = input("Answer is Correct or Wrong: \nY\t\tN")
        if response.lower() == "y":
            return True
        elif response.lower() == "n":
            return False


# adding game scores
def score_addition(player_number, game_name, game_owner, answer_status, lottery=0, bonus=0, penalty=0):
    games_points = {"guess_the_logo": 100, "who_is_who": 200}

    if answer_status:
        players_scores[player_number] = players_scores[player_number] + games_points[game_name]
    elif game_name == "penalty":
        players_scores[player_number] = players_scores[player_number] - penalty
    elif game_name == "bonus":
        players_scores[player_number] = players_scores[player_number] + bonus

    # if player gives the write answers then player is game owner
    if game_owner == player_number and answer_status == True:
        game_owners[game_name] = player_number
    elif game_owner == "None":
        pass
    elif game_owner != player_number:
        players_scores[game_owner] = players_scores[game_owner] + (games_points[game_name] / 4)

# defining penalty rules
def penalty(player, game_number):
    penalty_points = [10, 20, 30, 40, 50, 60]
    penalty_points_number = penalty_points[random.randint(0, 5)]
    if game_number - last_game_by_player[player] == 1:
        score_addition(player, "penalty", "None", False, 0, 0, penalty_points_number)
        return penalty_points_number
    elif game_number - last_game_by_player[player] == 2:
        score_addition(player, "penalty", "None", False, 0, 0, 20)
        return 20
    elif game_number - last_game_by_player[player] == 3:
        score_addition(player, "penalty", "None", False, 0, 0, penalty_points_number)
        return penalty_points_number
    elif game_number - last_game_by_player[player] == 4:
        score_addition(player, "penalty", "None", False, 0, 0, 40)
        return 40
    elif game_number - last_game_by_player[player] == 5:
        score_addition(player, "penalty", "None", False, 0, 0, penalty_points_number)
        return penalty_points_number
    elif game_number - last_game_by_player[player] == 6:
        score_addition(player, "penalty", "None", False, 0, 0, 60)
        return 60


def bonus(player, game_number):
    bonus_points = [10, 20, 30, 40, 50, 60]
    bonus_points_number = bonus_points[random.randint(0, 5)]
    if game_number - last_game_by_player[player] == 1:
        score_addition(player, "bonus", "None", False, 0, bonus_points_number, 0)
        return bonus_points_number
    elif game_number - last_game_by_player[player] == 2:
        score_addition(player, "bonus", "None", False, 0, 20, 0)
        return 20
    elif game_number - last_game_by_player[player] == 3:
        score_addition(player, "bonus", "None", False, 0, bonus_points_number, 0)
        return bonus_points_number
    elif game_number - last_game_by_player[player] == 4:
        score_addition(player, "bonus", "None", False, 0, 40, 0)
        return 40
    elif game_number - last_game_by_player[player] == 5:
        score_addition(player, "bonus", "None", False, 0, bonus_points_number, 0)
        return bonus_points_number
    elif game_number - last_game_by_player[player] == 6:
        score_addition(player, "bonus", "None", False, 0, 60, 0)
        return 60


# checks who is the owner of particular game
def who_is_game_owner(game_number, player):
    if game_owners[games_name_with_codes[game_number]] == None:
        return player
    else:
        return game_owners[games_name_with_codes[game_number]]


# check remaining turns
def update_remaining_chances(player, game_number, last_game):
    players_remaining_chances[player] = players_remaining_chances[player] - (game_number - last_game)
    return players_remaining_chances[player]


while True:
    for player in range(1, number_of_players + 1):
        if players_remaining_chances[player] >= 0:
            dice_number = int(input("Enter the Dice Number of player " + str(player) + " :"))
            game_number=dice_number+last_game_by_player[player]
            if game_number >= 28:
                update_remaining_chances(player, game_number, last_game_by_player[player])
                print("Player " + str(player) + " has completed his round")
                continue
            elif game_number == 4 or game_number == 18:
                update_remaining_chances(player, game_number, last_game_by_player[player])
                print("Penalty! of ", penalty(player, game_number))
                continue
            elif game_number == 11 or game_number == 18:
                update_remaining_chances(player, game_number, last_game_by_player[player])
                print("Bonus! of ", bonus(player, game_number))
                continue
            game_owner = who_is_game_owner(game_number, player)
            score_addition(player, games_name_with_codes[game_number], game_owner, game_chooser(game_number))
            update_remaining_chances(player, game_number, last_game_by_player[player])

            last_game_by_player[player] = game_number


        else:
            continue

    ifBreak = input("End game: Y or N")
    if ifBreak.lower() == "y":
        for i in range(1, number_of_players + 1):
            print("Score of player " + str(i) + " is " + str(players_scores[i]))

        break
