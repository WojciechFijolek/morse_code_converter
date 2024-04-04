from morse_code import morse_code_dict


def get_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None


class Converter:
    def __init__(self):
        self.dictionary = morse_code_dict
        self.input_message = ''
        self.output_message = ''
        self.words_list = []
        self.word_space = '       '    # seven units / space between encode words
        self.character_space = '   '    # three units / space between encode characters

    def encode(self, message):
        self.output_message = ''
        self.input_message = message.lower()
        self.words_list = self.input_message.split()
        for word in self.words_list:
            if self.words_list.index(word) != 0:
                self.output_message += '       '
            for position, character in enumerate(word):
                if position != 0:
                    self.output_message += self.character_space
                self.output_message += self.dictionary[character]
        print(self.output_message)

    def decode(self, message):
        self.output_message = ''
        self.words_list = message.split(self.word_space)
        for word in self.words_list:
            if self.words_list.index(word) != 0:
                self.output_message += ' '  # one unit / space between decode words
            character_list = word.split(self.character_space)
            for character in character_list:
                self.output_message += get_key_by_value(self.dictionary, character)
        print(self.output_message)