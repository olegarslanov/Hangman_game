"""
Here I create sql "Score_table" for Hangman game
"""

from sqlalchemy.orm import sessionmaker
from models import engine, Player

Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""


def login_player():
    """
    Choice db action
    """

    while True:
        choice = input(
            "Please enter: \n1 - login player \n2 - register new player"
            "\n3 - play without registration \n4 - show Score Table \n:"
        )

        if choice == str(1):
            nickname = input("Please enter Your nickname:")
            players = session.query(Player).all()

            player_found = False

            for player in players:
                if nickname == player.nickname:
                    print(f"Lets play {nickname}. Your score will be saved.")
                    player_found = True
                    player_id = player.id
                    return player_id

            if not player_found:
                print("Player doesn't exist. Please register a new player.")

        elif choice == str(2):
            register_new_player()

        elif choice == str(3):
            print("You playing without registration. Your score will not be saved.")
            break

        elif choice == str(4):
            display_score_table()

        else:
            print("Input correct letter. Please enter only: 1, 2, 3, or 4")


# def find_existing_player():
#     # player_id = None

#     nickname = input("Please enter Your nickname:")
#     players = session.query(Player).all()

#     player_found = False

#     for player in players:
#         if nickname == player.nickname:
#             print(f"Lets play {nickname}. Your score will be saved.")
#             player_found = True
#             player_id = player.id
#             return player_id

#     if not player_found:
#         print("Player doesn't exist. Please register a new player.")


def register_new_player():
    while True:
        try:
            nickname = input("Please enter nickname:")
            while len(nickname) < 4:
                nickname = input(
                    "Nickname should be at least 4 characters long."
                    "Please enter Your nickname:"
                )
            name = input("Please enter name:")
            surname = input("Please enter surname:")
            email = input("Please enter email:")
            played = 0
            won = 0
            lose = 0

            player = Player(nickname, name, surname, email, played, won, lose)
            session.add(player)
            session.commit()
            print("Player successfully added.")
            break
        except Exception as e:
            print(f"An error ocured: {e}. Please enter correct data.")


def display_score_table():
    players = session.query(Player).all()
    print("\n        Score Table         ", "\n----------------------------")
    for player in players:
        print(player)
