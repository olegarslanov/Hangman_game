from alphabet import alphabet

guess_letter_word = input("Please guess letter, or word:")


def is_letter_alphabet():
    for letter in alphabet:
        if letter == guess_letter_word:
            return True
