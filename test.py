hangman_parts = [
    """
     ________
    |       |
    |
    |
    |
    |
    |
    """,
    """
     ________
    |       |
    |       O
    |
    |
    |
    |
    """,
    """
     ________
    |       |
    |       O
    |       |
    |
    |
    |
    """,
    """
     ________
    |       |
    |       O
    |      /|
    |
    |
    |
    """,
    """
     ________
    |       |
    |       O
    |      /|\\
    |
    |
    |
    """,
    """
     ________
    |       |
    |       O
    |      /|\\
    |      /
    |
    |
    """,
    """
     ________
    |       |
    |       O
    |      /|\\
    |      / \\
    |
    |
    """,
]


def draw_hangman(tries):
    print(hangman_parts[tries])


def main():
    word = "hangman"
    guessed_word = ["_"] * len(word)
    tries = 0

    while "_" in guessed_word and tries < len(hangman_parts):
        draw_hangman(tries)
        print(" ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            tries += 1

    if "_" not in guessed_word:
        print("Congratulations! You've guessed the word:", word)
    else:
        draw_hangman(tries)
        print("Sorry, you've run out of tries. The word was:", word)


if __name__ == "__main__":
    main()
