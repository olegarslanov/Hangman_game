import random
from data import fruits, animals, numbers, countries
from word_to_row import word_to_row


class LifesCounter:
    def __init__(self, lifes=10):
        self.lifes = lifes

    def reduce_lifes(self):
        self.lifes -= 1

    def get_result(self):
        return self.lifes


class WordGuessGame:
    def __init__(self, random_word):
        self.random_word = random_word
        self.word_mask = [" " for _ in random_word]
        self.lifes_counter = LifesCounter()

    def guess_mask_modificate(self):
        while self.lifes_counter.get_result() > 0:
            guess_letter = input("Please guess letter:")
            letter_found = False
            word_lenght = len(self.random_word)
            count_number = 0
            while count_number < word_lenght:
                if self.random_word[count_number] == guess_letter:
                    self.word_mask[count_number] = guess_letter
                    letter_found = True
                count_number += 1
            if not letter_found:
                self.lifes_counter.reduce_lifes()
                print(f"Lifes left: {self.lifes_counter.get_result()}")
                if self.lifes_counter.get_result() == 0:
                    print("You lose. Game over")
                    break
            print(word_to_row("".join(self.word_mask)))
            if "".join(self.word_mask) == self.random_word:
                print("Congratulations, you guessed the word!")
                break


# CLI
print("Welcome to the game 'Hangman'")
print(
    "You can learn how to play this game by clicking on this link: https://www.youtube.com/watch?v=leW9ZotUVYo"
)
print("First please choose content of spelled words:")

while True:
    content_choice = input(
        "fruits please enter - A, \nanimals please enter - B, \nnumbers please enter - C, \ncountries please enter - D :\n"
    )

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


print(random_word)  # cia print mokymo tikslais
game = WordGuessGame(random_word)

# Paverciu zodi i viena eilute ir isvedu lentele (paslepus visas raides)
print(word_to_row(game.word_mask))

game.guess_mask_modificate()
