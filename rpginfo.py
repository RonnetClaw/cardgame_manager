class RPGInfo():

    author = "RK"

    def __init__(self, game_title):
        self.game_title = game_title

    def welcome(self):
        print("Welcome to " + self.game_title)

    @staticmethod
    def info():
        print("Made using the OOP RPG game creator (c) RK")

    @classmethod
    def credits(cls):
        print("Thanks for playing!")
        print("Created by " + cls.author)