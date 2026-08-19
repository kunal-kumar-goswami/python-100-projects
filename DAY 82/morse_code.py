def main():
    # CONSTANTS
    MINOR_SPACE = " "      # between letters
    MAJOR_SPACE = "   "    # between words

    # MORSE CODE DICTIONARY (built once, lookup is O(1) instead of scanning tuple keys)
    BOOK = {
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '@': '.--.-.',
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',
    }

    WELCOME_MESSAGE = '''
    +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+
    |M|o|r|s|e| |C|o|d|e| |E|n|c|o|d|e|r|
    +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+
    '''

    GOODBYE_MESSAGE = '''
    +-+-+-+-+-+-+-+
    |G|o|o|d|B|y|e|
    +-+-+-+-+-+-+-+
    '''

    # FUNCTIONS
    def get_morse(text):
        """
        Converts a string into its Morse code equivalent.
        Letters within a word are separated by MINOR_SPACE,
        words are separated by MAJOR_SPACE.
        Unknown characters are skipped silently.
        """
        words = text.upper().split(' ')
        encoded_words = []

        for word in words:
            letters = [BOOK[char] for char in word if char in BOOK]
            encoded_words.append(MINOR_SPACE.join(letters))

        return MAJOR_SPACE.join(encoded_words)

    def get_user_input():
        return input('Please provide a String to convert?\n')

    def wants_to_continue():
        while True:
            response = input('Would you like to encode another message?\nType (Y/N)\n').strip().lower()
            if response in ('y', 'n'):
                return response == 'y'
            print("Please enter Y or N.")

    # MAIN LOOP
    print(WELCOME_MESSAGE)
    print('Welcome to Morse Code Encoder !!')

    while True:
        user_response = get_user_input()
        print(get_morse(user_response))

        if not wants_to_continue():
            print('Thank you for using Morse Code Converter')
            print(GOODBYE_MESSAGE)
            break


if __name__ == '__main__':
    main()