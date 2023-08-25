"""
This module contains functions for hangman game.
"""

import random
from data import fruits, animals, numbers, countries
from word_to_row import word_to_row
from hangman_pictures import hangman_parts, GAME_WELCOME


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
        """
        get counter result.
        """
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
        """
        get counter result.
        """
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
        """
        show word mask first.
        """
        return word_to_row(self.word_mask)

    def guess_word(self) -> bool:
        """
        Checks guess letter, or word. Print hangman pictures and how much
        lifes is left. Checks if the word is guessed.
        """
        while self.lifes_counter.get_result() > 0:
            guess_letter_word = input("Please guess letter, or word:")

            if len(guess_letter_word) == 1:
                self.is_letter_guesed(guess_letter_word)
            elif len(guess_letter_word) > 1:
                self.is_word_guessed(guess_letter_word)
            else:
                print("Something wrong. Please try one more time")

            self.print_game_status()

            if self.word_mask == self.random_word:
                return True

        return False

    def is_letter_guesed(self, guess_letter) -> str:
        """
        update word mask.
        enumerate() funkcija Pythone leidzia pereiti per seka ir
        kartu gauti ir elemento indeksa bei pati elementa
        """
        letter_found = False
        for index, letter in enumerate(self.random_word.lower()):
            if letter == guess_letter.lower():
                self.word_mask[index] = self.random_word[index]
                letter_found = True
        if not letter_found:
            self.lifes_counter.reduce_lifes()
            self.hangman_parts_counter.count_parts()

    def is_word_guessed(self, guess_word) -> str:
        """
        check if the word is guessed.
        """
        if self.random_word.lower() == guess_word.lower():
            self.word_mask = self.random_word

        else:
            self.lifes_counter.reduce_lifes()
            self.hangman_parts_counter.count_parts()
            print(f"Sorry guess word is not: {guess_word}")

    def print_game_status(self) -> str:
        """
        Print word mask, lifes left, hangman pictures
        """
        print(word_to_row("".join(self.word_mask)))

        if self.word_mask != self.random_word:
            print("Lifes left:", self.lifes_counter.get_result())
            print(hangman_parts[self.hangman_parts_counter.get_result()])


def main():
    """
    App launch function.
    """
    print(GAME_WELCOME)
    print(
        "You can learn how to play this game by clicking on this link: \n"
        "https://www.youtube.com/watch?v=leW9ZotUVYo"
    )
    print("\nFirst please choose content of spelled words:")
    while True:
        content_choice = input(
            "fruits please enter - A, \nanimals please enter - B"
            "\nnumbers please enter - C, \ncountries please enter - D:\n"
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
        print("Congratulations. You guessed the word!")
    else:
        print(f"You lose. Game over. Word is: {random_word}")


if __name__ == "__main__":
    main()
