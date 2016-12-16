
from WordPicker import WordPicker
from Filereader import FileReader

from abc import ABC, abstractmethod

class Mediator(ABC):

    def __init__(self):
        self.hero = Hero(self)
        self.hangman = Hangman(self)
        self.gallows = Gallows(self)
        self.criminal = Criminal(self)
        self.word_guessed = False
        self.gallows_completed = False

    def play_game(self):
        self.running = True
        while not self.word_guessed and not self.gallows_completed:
            print(self.hangman.get_masked_word())
            self.guessed_letter = self.hero.guess_letter()
            self.hangman.ask_letter(self.guessed_letter)

    def exit(self):
        self.running = False

    @abstractmethod
    def get_word_list(self):
        pass

    @abstractmethod
    def guess_letter(self):
        pass

    @abstractmethod
    def notify_same_guess(self):
        pass

    @abstractmethod
    def notify_wrong_guess(self):
        pass

    @abstractmethod
    def notify_word_guessed(self):
        pass

    @abstractmethod
    def notify_gallows_completed(self):
        pass

class TextUI(Mediator):

    def get_word_list(self):
        return FileReader('hangmanwords.txt').get_Line_List()

    def guess_letter(self):
        return input('Guess a letter.\n')

    def notify_same_guess(self, guess):
        print('You have already guessed \'{0}\'. Enter something different!'.format(guess))

    def notify_wrong_guess(self):
        self.gallows.add_part()
        if self.gallows.get_attempts_remaining() > 1:
            print('That was wrong. You have', self.gallows.get_attempts_remaining(), 'chances remaining.')
        elif self.gallows.get_attempts_remaining() == 1:
            print('That was wrong. You have', self.gallows.get_attempts_remaining(), 'chance remaining.')

    def notify_word_guessed(self):
        self.word_guessed = True
        print('Hurrah! You saved the man!')

    def notify_gallows_completed(self):
        self.gallows_completed = True
        print('Uh oh. The man\'s been hanged!')



class Hero:

    def __init__(self, mediator):
        self.mediator = mediator

    def guess_letter(self):
        self.user_input = self.mediator.guess_letter()
        return self.user_input


class Hangman:
    correct_letter_count = 0
    letters_guessed = []

    def __init__(self, mediator):
        self.mediator = mediator
        word_list = self.mediator.get_word_list()
        self.secret_word = WordPicker(word_list).pick_at_random()
        self.masked_word = []
        for i in range (0,len(self.secret_word)):
            self.masked_word.append('_')



    def get_secret_word(self):
        return self.secret_word

    def get_masked_word(self):
        return ''.join(self.masked_word)

    def ask_letter(self, input):
        is_letter_there = False
        self.same_guess = False
        for i in range(0, len(self.letters_guessed)):
            if input == self.letters_guessed[i]:
                self.same_guess = True
        self.letters_guessed.append(input)
        if not self.same_guess:
            if len(input) == 1:
                for i in range(0, len(self.secret_word)):
                    if input == self.secret_word[i]:
                        self.correct_letter_count += 1
                        self.masked_word[i] = input
                        is_letter_there = True
                if self.correct_letter_count >= len(self.secret_word):
                    self.mediator.notify_word_guessed()
                if not is_letter_there:
                    self.mediator.notify_wrong_guess()
            elif input == self.secret_word:
                self.mediator.notify_word_guessed()
            else:
                self.mediator.notify_wrong_guess()
        else:
            self.mediator.notify_same_guess(input)

class Gallows:

    parts_added = 0

    def __init__(self, mediator):
        self.mediator = mediator

    def add_part(self):
        self.parts_added += 1
        if self.parts_added >= 5:
            self.mediator.notify_gallows_completed()

    def get_attempts_remaining(self):
        return 5 - self.parts_added

class Criminal:

    def __init__(self, mediator):
        self.mediator = mediator


text_UI = TextUI()
#text_UI.play_game()
