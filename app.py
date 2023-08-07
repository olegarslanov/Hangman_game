import random
from data import fruits, animals, numbers, countries
from answer_table import create_word_mask, replace_space_to_letter


# CLI
print("This is a game 'Hangman'")
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

print(random_word)
# Paverčiame žodį į vieną eilutę ir išvedame lentelę (paslepus visas neatspetas raides)
create_word_mask(random_word)

guess_letter = input(
    "Please guess letter(letters only from english alphabet), or word:\n"
)

replace_space_to_letter(random_word, guess_letter)
