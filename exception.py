class NoSuchOption(Exception):
    def __str__(self):
        return """Choice not recognized, please try again"""


class NotSuchBookType(Exception):
    def __str__(self):
        return """There is no such type of book, please try again"""


class InvalidOption(Exception):
    def __str__(self):
        return "Please choose a valid number between 1-13"


class NotInteger(Exception):
    def __str__(self):
        return """Please enter an integer for the last prompt"""
