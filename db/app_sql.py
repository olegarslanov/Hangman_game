"""
Here I made sql "Score_table" for Hangman game
"""

from sqlalchemy.orm import sessionmaker
from models import engine, Player

Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""


def player_login():
    """
    Choice db action
    """

    while True:
        choice = int(
            input(
                "Please enter: \n1 - login player \n2 - register new player \n3 - play without registration \n4 - show Score Table \n:"
            )
        )

        if choice == 1:
            nickname = input("Please enter Your nickname:")

            players = session.query(Player).all()
            player_found = False
            for player in players:
                if nickname == player.nickname:
                    print(f"Lets play again {nickname}")

                    player_found = True
                    return player.id, False

            if not player_found:
                print("Player doesn't exist. Please register a new player.")

        if choice == 2:
            while True:
                try:
                    nickname = input("Please enter nickname:")
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

        if choice == 3:
            print("You playing without registration. Your score will not be saved.")
            break

        if choice == 4:
            players = session.query(Player).all()

            print("\n        Score Table         ", "\n----------------------------")
            for player in players:
                print(player)


print(player.id)


def update_player_score():
    """
    Update db (played, won, lose)
    """

    # player = session.query(Player).filter_by(id).first()

    player = session.query(Player).filter_by(player.id).first()
    player.played += 1
    session.commit()

    print("\n        Score Table         ", "\n----------------------------")
    for player in players:
        print(player)
