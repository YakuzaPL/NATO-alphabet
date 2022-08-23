import pandas


nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

npa_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}


def generate_phonetic():
    word = input("Wha would you like to spell?: ")

    try:
        spelling_list = [npa_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters in te alfabet please!")
        generate_phonetic()
    else:
        print(spelling_list)


generate_phonetic()