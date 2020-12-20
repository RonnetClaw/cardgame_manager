class Character():

    discarded_chars = []
    hp = 3

    # Initialize a Character
    def __init__(self, char_name, words=None):
        """
        Initialize a Character
        :param char_name:
        :param words:
        """
        self.char_name = char_name
        self.words = words

    # BASICS:
    # Set Character name
    def set_char_name(self, char_name):
        """
        Set Character name
        :param char_name:
        :return:
        """
        self.char_name = char_name

    # Get Character name
    def get_char_name(self):
        """
        Get Character name
        :return:
        """
        return self.char_name

    # Set Character words
    def set_char_words(self, words):
        """
        Set Character words
        :param words:
        :return:
        """
        self.words = words

    # Get Character words
    def get_char_words(self):
        """
        Get Character words
        :return:
        """
        return self.words

    # Talk to Character
    def talk(self):
        """
        Talk to a Character
        :return:
        """
        if self.words is not None:
            print(self.get_char_name() + " says: " + self.get_char_words())
        else:
            print(self.get_char_name() + " does not want to talk to you!")

    # Fight the Character
    def fight(self):
        """
        Fight the Character
        :return:
        """
        print(self.get_char_name() + " does not want to fight you!")

    # CHARACTER, ROOM management
    # Add Character to Room
    def add_char_to_room(self, room):
        """
        Add Character to Room
        :param room:
        :return:
        """
        room.chars.append(self)

    # Delete Character from Room, moving to Discard pile
    def delete_char_from_room(self, room):
        """
        Delete Character from Room, moving to Discard Pile
        :param room:
        :return:
        """
        if room.chars:
            pos = room.chars.index(self)
            Character.discarded_chars.append(room.chars.pop(pos))
        else:
            print("There's nobody here!")

class Enemy(Character):

    # Initializing an Enemy (Character with special attributes, methods)
    def __init__(self, char_name, words=None):
        """
        Initialize Enemy Character with special attributes, methods
        :param char_name:
        :param words:
        """
        super().__init__(char_name, words)
        self.weakness = None

    # Setting Weakness to Enemy
    def set_weakness(self, weakness):
        """
        Setting Weakness to Enemy
        :param weakness:
        :return:
        """
        self.weakness = weakness

    # To get Weakness of an Enemy
    def get_weakness(self):
        """
        Get Weakness of an Enemy
        :return:
        """
        return self.weakness

    # To Fight an Enemy with combat_item
    def fight(self, combat_item=None):
        """
        Fight an Enemy with combat_item
        :param combat_item:
        :return:
        """
        print("Fighting " + self.get_char_name() + ": ")
        while Character.hp > 0:
            if combat_item is None or combat_item != self.weakness:
                command = input("Enter your combat weapon: ")
                if command == self.weakness:
                    print("You beat " + self.get_char_name() + "! Congratulations!")
                    break
                elif command == "flee":
                    print("You run away!")
                    break
                else:
                    print(self.get_char_name() + " beat you!")
                    Character.hp = Character.hp - 1
                    if Character.hp > 0:
                        print("Try again!")
                        print("Your HP now is: (" + str(Character.hp) + "/3)")
                        print("You will die when HP = 0. Type flee to escape!")
            else:
                print("You beat " + self.get_char_name() + "! Congratulations!")
                break
        else:
            print("You have died!")
            exit()
