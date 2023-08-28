"""
created to avoid problems with a cyclic module import situation
"""

import sys
import random

from sqlalchemy.orm import sessionmaker

sys.path.append("C:\\Users\\olega\\projects\\Hangman_game\\db")

from models import engine, Player
from app_sql2 import login_player
from data import fruits, countries, numbers, animals
from app import WordGuessGame
from hangman_pictures import GAME_WELCOME


def main():
    """
    App launch function.
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    print(GAME_WELCOME)
    print(
        "You can learn how to play this game by clicking on this link: \n"
        "https://www.youtube.com/watch?v=leW9ZotUVYo"
    )

    player_id = login_player()

    print("\nFirst please choose content of spelled words:")

    while True:
        content_choice = input(
            "fruits please enter - A, \nanimals please enter - B"
            "\nnumbers please enter - C, \ncountries please enter - D:\n"
        ).upper()

        if content_choice == "A":
            random_word = random.choice(fruits)
            break
        if content_choice == "B":
            random_word = random.choice(animals)
            break
        if content_choice == "C":
            random_word = random.choice(numbers)
            break
        if content_choice == "D":
            random_word = random.choice(countries)
            break
        else:
            print("Input correct letter. Please enter only: A, B, C, or D")

    game = WordGuessGame(random_word)
    game.word_mask_first()
    return_result = game.guess_word()

    player = session.get(Player, player_id)  # use user ID
    player.played += 1

    if return_result:
        print("Congratulations. You guessed the word!")
        player.won += 1
    else:
        print(f"You lose. Game over. Word is: {random_word}")
        player.lose += 1

    session.commit()

    players = session.query(Player).all()
    print("\n        Score Table         ", "\n----------------------------")
    for player in players:
        print(player)


if __name__ == "__main__":
    main()
