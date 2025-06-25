
class InvalidEmailError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Error: Enter a valid Email"