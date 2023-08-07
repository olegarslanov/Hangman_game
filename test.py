def create_word_mask(word):
    word_mask = ""
    for letter in word:
        if letter == guess_letter:
            word_mask += letter
        else:
            word_mask += " "
    return word_mask


guess_letter = "Y"

my_word = "PYTHON"
word_mask = create_word_mask(my_word)
print(word_mask)
