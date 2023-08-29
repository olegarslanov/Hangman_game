"""
Here I made sql "Score_table" for Hangman game
"""
# import dataclasses
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///db/Score_table.db")
Base = declarative_base()


class Player(Base):
    """
    Create class 'Project' with atributes (id, name, surname, email,
    played, won, lose)
    Method 'repr' return row with same atributes
    """

    __tablename__ = "Score Table"
    id = Column(Integer, primary_key=True)
    nickname = Column("Nickname", String)
    name = Column("Name", String)
    surname = Column("Surname", String)
    email = Column("Email", String)
    played = Column("Played", Integer)
    won = Column("Won", Integer)
    lose = Column("Lose", Integer)

    def __init__(
        self,
        nickname: str,
        name: str,
        surname: str,
        email: str,
        played: int,
        won: int,
        lose: int,
    ):
        self.name = name
        self.nickname = nickname
        self.surname = surname
        self.email = email
        self.played = played
        self.won = won
        self.lose = lose

    def __repr__(self):
        return (
            f"id: {self.id}, nickname: {self.nickname}\n"
            f"name: {self.name}, surname: {self.surname}\n"
            f"email: {self.email}\n"
            f"played: {self.played}, won: {self.won}, lose: {self.lose}"
            "\n----------------------------"
        )


Base.metadata.create_all(engine)
