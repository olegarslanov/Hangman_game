# from prettytable import PrettyTable

# random_word = "dog"


# # zodi iterpiu i lentele
# def word_to_row(word):
#     # sukuriu lentele su viena eilute
#     table = PrettyTable()

#     # pridedu kiekviena zodzio raide i lenteles langeli
#     for letter in word:
#         table.add_column("", [f"{letter}"])

#     # nustatau lenteliu liniju sankirtos tasko simboli
#     table.junction_char = "+"

#     # nustatau, kad lentelei bus nubrezti remeliai
#     table.border = True

#     # grazinu lentele kaip vieną eilutę
#     return table.get_string(header=False, border=True)


# def lifes_counter():
#     lifes = 10

#     def reduce_lifes():
#         nonlocal lifes  # kai naudoju "nonlocal" raktažodi vidineje funkcijoje, pasakau, kad noriu modifikuoti kintamaji isor. funkcijoje, o ne kurti nauja kintamaji vidineje funkcijoje
#         lifes -= 1

#     def get_result():
#         return lifes

#     return {
#         "reduce lifes": reduce_lifes,
#         "get result": get_result,
#         "lifes value": lifes,
#     }


# # random zodzio raides paverciu i tarpus
# def get_random_word_mask(random_word):
#     word_mask = ""
#     for _ in random_word:
#         word_mask += " "
#     print(word_to_row(word_mask))


# def guess_mask_modificate(random_word):
#     word_mask = [" " for _ in random_word]  # sukuriu pradini word_mask sarasa
#     get_random_word_mask(random_word)
#     lifes_rest = lifes_counter()
#     while lifes_rest["get result"]() > 0:
#         guess_letter = input("Please guess letter:")
#         letter_found = False
#         word_lenght = len(random_word)
#         count_number = 0
#         while count_number < word_lenght:
#             if random_word[count_number] == guess_letter:
#                 word_mask[count_number] = guess_letter
#                 letter_found = True
#             count_number += 1
#         if not letter_found:
#             lifes_rest["reduce lifes"]()
#             print(f'Lifes left: {lifes_rest["get result"]()}')
#             if lifes_rest["get result"]() == 0:
#                 print("You loose. Game over")
#                 break
#         print(
#             word_to_row("".join(word_mask))
#         )  # sudedu saraso elementus i viena eilute, atnaujinus simbolius, kai atspejama raide
#         if "".join(word_mask) == random_word:
#             print("Congratulations, you guessed the word!")
#             break


# guess_mask_modificate(random_word)
