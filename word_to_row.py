from prettytable import PrettyTable  # biblioteka skirta kurti lenteles


# iterpiu zodi i lentele
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
