from alphabet import alphabet, morse_alphabet
import pyperclip


class TextToMorse:
    def __init__(self):
        self.alphabet = alphabet
        self.morse_alphabet = morse_alphabet
        self.start()
        print('Goodbye 👋')

    def start(self):
        is_app_on = True
        while is_app_on:
            user_input = input('Do you want to use the text to morse code converter?\nType 0 for no and 1 for yes\n')
            if user_input == '1':
                self.choose_method()
            elif user_input == '0':
                is_app_on = False
            else:
                print('Invalid input. Please type 0 or 1')

    def choose_method(self):
        is_app_on = True
        while is_app_on:
            user_input = input('Welcome to the text to morse code converter!\n'
                               'Type 0 to return to the main menu\n1 to encode text to morse code\n'
                               '2 to decode morse code to text\n')
            if user_input == '1':
                self.encode()
            elif user_input == '2':
                self.decode()
            elif user_input == '0':
                is_app_on = False
            else:
                print('Invalid input. Please type 0, 1 or 2')

    def encode(self):
        text = input('Please type text that needs to be converted\n')
        text_list = list(text)
        morse_list = []
        for char in text_list:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                morse_char = self.morse_alphabet[index]
                morse_list.append(morse_char)
            else:
                morse_list.append(char)
        morse_text = ' '.join(morse_list)
        pyperclip.copy(morse_text)
        print(morse_text)
        print('Morse code has been copied to the clipboard!')

    def decode(self):
        morse_text = input('Please type morse code that needs to be converted\n')
        morse_list = morse_text.split(' ')
        text_list = []
        for char in morse_list:
            if char in self.morse_alphabet:
                index = self.morse_alphabet.index(char)
                text_char = self.alphabet[index]
                text_list.append(text_char)
            elif char == '':
                text_list.append(' ')
            else:
                text_list.append(char)
        text = ''.join(text_list)
        # pyperclip.copy(text)
        print(text)
        # print('Text has been copied to the clipboard!')
