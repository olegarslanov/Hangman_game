#  modifikuoja uzmaskuota zodi
class GuessWordMask:
    def guess_mask_modificate(self, random_wor d):
        word_mask = [" " for _ in random_word]  # sukuriu pradini word_mask sarasa
        get_random_word_mask(random_word)

        while lifes_counter.get_result() > 0:
            guess_letter = input("Please guess letter:")
            letter_found = False
            word_lenght = len(random_word)
            count_number = 0

            while count_number < word_lenght:
                if random_word[count_number] == guess_letter:
                    word_mask[count_number] = guess_letter
                    letter_found = True
                count_number += 1

            if not letter_found:
                lifes_counter.reduce_lifes()
                print(f"Lifes left: {lifes_counter.get_result()}")
                if lifes_counter.get_result() == 0:
                    print("You loose. Game over")
                    break

            print(
                word_to_row("".join(word_mask))
            )  # sudedu saraso elementus i viena eilute, atnaujinus simbolius, kai atspejama raide

            if "".join(word_mask) == random_word:
                print("Congratulations, you guessed the word!")
                break
