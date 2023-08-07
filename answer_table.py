from prettytable import PrettyTable


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


# zodi iterpiu i lentele
def word_to_row(word):
    # sukuriu lentele su viena eilute
    table = PrettyTable()

    # pridedu kiekviena zodzio raide i lenteles langeli
    for letter in word:
        table.add_column("", [f"{letter}"])

    # nustatau lenteliu liniju sankirtos tasko simboli
    table.junction_char = "+"

    # nustatau, kad lentelei bus nubrezti remeliai
    table.border = True

    # grazinu lentele kaip vieną eilutę
    return table.get_string(header=False, border=True)


# zodzio raides paverciu i tarpus
def create_word_mask(word):
    # pakeiciu raidziu vieta žodžio 'word' tekste i tarpus
    word_mask = "".join([" " for _ in word])
    print(word_to_row(word_mask))


def replace_space_to_letter(word, guess_letter):
    word_mask = ""
    for letter in word:
        if letter == guess_letter:
            word_mask += letter
        else:
            word_mask += " "
    print(word_to_row(word_mask))
