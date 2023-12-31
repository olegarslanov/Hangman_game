"""
This module contains functions for 'Hangman' game.
"""

from word_to_row import word_to_row
from hangman_pictures import hangman_parts
from alphabet import alphabet


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

    def __init__(self, random_word: str) -> None:
        self.random_word = random_word
        self.word_mask = [" " for _ in random_word]
        self.lifes_counter = LifesCounter()
        self.hangman_parts_counter = HangmanPartsCounter()
        self.guess_letter_word = None
        self.used_letters = []

    def word_mask_first(self) -> str:
        """
        show word mask first.
        """
        print(word_to_row(self.word_mask))

    def guess_word(self) -> bool:
        """
        Checks guess letter, or word. Print hangman pictures and remaining
        lives. Checks if the word is guessed.
        """
        while self.lifes_counter.get_result() > 0:
            self.guess_letter_word = input("Please guess letter, or word:").lower()

            if len(self.guess_letter_word) == 1 and self.is_letter_alphabet():
                if self.is_letter_used(self.guess_letter_word):
                    print("! Letter is used. Please enter another letter !")
                else:
                    self.is_letter_guesed(self.guess_letter_word)
            elif len(self.guess_letter_word) > 1:
                self.is_word_guessed(self.guess_letter_word)
            else:
                print(
                    "!!! In this game You can enter only alphabet letters."
                    "Symbols is not accepted. Please enter letter !!!"
                )

            self.used_letters.append(self.guess_letter_word)

            self.print_game_status()

            if ("".join(self.word_mask).lower()) == self.random_word.lower():
                return True

        return False

    def is_letter_alphabet(self) -> bool:
        """Check is letter in alphabet"""
        for letter in alphabet:
            if letter == self.guess_letter_word:
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

    def is_letter_used(self, guess_letter) -> bool:
        """Check if letter used before."""
        if guess_letter in self.used_letters:
            return True
        return False

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

        if ("".join(self.word_mask)) != self.random_word:
            print("Lifes left:", self.lifes_counter.get_result())
            print(hangman_parts[self.hangman_parts_counter.get_result()])
