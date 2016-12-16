import random

class WordPicker:

    def __init__(self, list):
        self.list = list

    def pick_at_random(self):
        return random.choice(self.list)

