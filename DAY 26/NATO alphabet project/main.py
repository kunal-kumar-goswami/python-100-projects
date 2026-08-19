import pandas

data = pandas.read_csv("/python/100 Days of Code/DAY 26/NATO alphabet project/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        op_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry , only letter in the alphabet please. ")
        generate_phonetic()
    else:
        print(op_list)

generate_phonetic()