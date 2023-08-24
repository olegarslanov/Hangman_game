"""
This module contains functions for hangman game.
"""

import random
from data import fruits, animals, numbers, countries
from word_to_row import word_to_row
from hangman_pictures import hangman_parts


class LifesCounter:
    """
    This class contens the lifes counter.
    """

    def __init__(self, lifes=10) -> None:
        self.lifes = lifes

    def reduce_lifes(self) -> int:
        """
        the purpose of the reduce_lifes method is to
        decrease the value of the lifes attribute of an object by 1.
        """
        self.lifes -= 1

    def get_result(self) -> int:
        return self.lifes


class HangmanPartsCounter:
    """
    This class contains the Hangman parts counter from hangman_pictures.py.
    """

    def __init__(self, count=0) -> None:
        self.count = count

    def count_parts(self) -> int:
        """
        the purpose of the count_parts method is to
        increase the value of the hangman_parts list by 1.
        """
        self.count += 1

    def get_result(self) -> int:
        return self.count


class WordGuessGame:
    """
    This class contains functions for hangman game.
    """

    def __init__(self, random_word) -> None:
        self.random_word = random_word
        self.word_mask = [" " for _ in random_word]
        self.lifes_counter = LifesCounter()
        self.hangman_parts_counter = HangmanPartsCounter()

    def word_mask_first(self) -> str:
        return word_to_row(self.word_mask)

    def guess_word(self) -> bool:
        while self.lifes_counter.get_result() > 0:
            # print(self.word_mask)
            guess_letter_word = input("Please guess letter, or word:")
            if len(guess_letter_word) == 1:
                self.update_word_mask(guess_letter_word)
            elif len(guess_letter_word) > 1:
                self.check_guess_word(guess_letter_word)
            else:
                print("Something wrong")

            self.print_game_status()

            if self.is_word_guessed():
                print(word_to_row(self.random_word))
                return True
        return False

    def update_word_mask(self, guess_letter) -> str:
        letter_found = False
        for index, letter in enumerate(self.random_word.lower()):
            # enumerate() funkcija Pythone leidzia pereiti per seka ir
            # kartu gauti ir elemento indeksa bei pati elementa
            if letter == guess_letter.lower():
                self.word_mask[index] = guess_letter
                letter_found = True
        if not letter_found:
            self.lifes_counter.reduce_lifes()
            self.hangman_parts_counter.count_parts()

    def check_guess_word(self, guess_word) -> str:
        if self.random_word.lower() == guess_word.lower():
            self.word_mask = guess_word
            return True
        else:
            self.lifes_counter.reduce_lifes()
            self.hangman_parts_counter.count_parts()
            print(f"Sorry guess word is not: {guess_word}")
            return False

    def is_word_guessed(self) -> bool:
        return "".join(self.word_mask).lower() == self.random_word.lower()

    def print_game_status(self) -> str:
        """
        Calculate the average of a list of numbers.

        Args:
        numbers (list): A list of numbers.

        Returns:
        float: The calculated average.
        """
        if not self.is_word_guessed():
            print(word_to_row("".join(self.word_mask)))
            print("Lifes left:", self.lifes_counter.get_result())
            print(hangman_parts[self.hangman_parts_counter.get_result()])


def main():
    """
    App launch function.
    """
    print(
        """
                    Welcome to the game:

             H  H
             H  H HHHH HHHH  HHH HHHH  HHHH HHH
             HHHH    H H  H H  H H H H    H H  H
             H  H  HHH H  H H  H H H H  HHH H  H
             H  H H  H H  H H  H H H H H  H H  H
             H  H HHHH H  H  HHH H H H HHHH H  H
                               H
                            HHH
        """
    )
    print(
        "You can learn how to play this game by clicking on this link: \n"
        "https://www.youtube.com/watch?v=leW9ZotUVYo"
    )
    print("\nFirst please choose content of spelled words:")
    while True:
        content_choice = input(
            "fruits please enter - A, \nanimals please enter - B"
            "\nnumbers please enter - C, \ncountries please enter - D"
        ).upper()

        if content_choice == "A":
            random_word = random.choice(fruits)
            break
        elif content_choice == "B":
            random_word = random.choice(animals)
            break
        elif content_choice == "C":
            random_word = random.choice(numbers)
            break
        elif content_choice == "D":
            random_word = random.choice(countries)
            break
        else:
            print("Input correct letter. Please enter only: A, B, C, or D")

    game = WordGuessGame(random_word)

    # print(random_word)  # mokymo tikslais
    print(game.word_mask_first())

    if game.guess_word():
        print("Congratulations, you guessed the word!")
    else:
        print(f"You lose. Game over. Word is: {random_word}")


if __name__ == "__main__":
    main()
