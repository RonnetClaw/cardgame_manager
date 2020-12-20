from item import Item
opp_dirs = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}


class Room():
    def __init__(self, room_name, room_desc=None):
        self.room_name = room_name
        self.room_desc = room_desc
        self.links = {}
        self.items = []
        self.chars = []

    # BASICS:
    # Set Room name
    def set_room_name(self, room_name):
        """
        Set Room name
        :param room_name:
        :return:
        """
        self.room_name = room_name

    # Get Room name
    def get_room_name(self):
        """
        Get Room name
        :return:
        """
        return self.room_name

    # Set Room desc
    def set_room_desc(self, room_desc):
        """
        Set Room desc
        :param room_desc:
        :return:
        """
        self.room_desc = room_desc

    # Get Room desc
    def get_room_desc(self):
        """
        Get Room desc
        :return:
        """
        return self.room_desc

    # Get Room details
    def get_room_details(self):
        """
        Get Room details
        :return:
        """
        print()
        print("Room: " + self.get_room_name() + ";", end=" ", flush=True)
        print(self.get_room_desc())
        self.get_links()
        print()
        self.get_chars()
        self.get_items()
        print()

    # LINKS:
    # Link Room to another Room + vice versa
    def link_room(self, room, direction):
        """
        Link Room to another Room and vice versa
        :param room:
        :param direction:
        :return:
        """
        self.links[direction] = room
        room.links[opp_dirs[direction]] = self

    # After prompt, move from one Room to another
    def move(self, direction):
        """
        After prompt, move from one Room to another
        :param direction:
        :return:
        """
        if direction in self.links:
            return self.links[direction]
        else:
            print("Oh, you can't go that way!")
            return self

    # Get all links from this Room
    def get_links(self):
        """
        Get all links from this Room
        :return:
        """
        print("Paths:", end=" ", flush=True)
        for i, links in enumerate(self.links, start=1):
            print("(" + str(i) + ") " + self.links[links].get_room_name() + " - " + links + ";", end=" ", flush=True)

    # ITEM, CHARACTER MANAGEMENT:
    # Add an Item to a Room
    def add_item(self, item):
        """
        Add an Item to a Room
        :param item:
        :return:
        """
        self.items.append(item)

    # Delete an Item from a Room
    def delete_item(self, item):
        """
        Delete an Item from a Room
        :param item:
        :return:
        """
        item.delete_item_from_room(self)

    # Get all Items in a Room
    def get_items(self):
        """
        Get all Items in a Room
        :return:
        """
        if self.items:
            print("Items in room:", end=" ", flush=True)
            for i, item in enumerate(self.items, start=1):
                print("(" + str(i) + ") " + item.get_item_name() + ";", end=" ", flush=True)
        else:
            print("Items in room: There's nothing else here!")

    # Pick an Item from Room
    def pick_item(self, item_name=None):
        """
        Pick an Item from Room
        :param item_name:
        :return:
        """
        if item_name is None:
            if self.items:
                print("Added " + self.items[0].get_item_name() + "...")
                Item.backpack.append(self.items.pop(0))
            else:
                print("Can't do that!")
        else:
            pos = self.items.index(item_name)
            print("Added" + item_name.get_item_name() + "...")
            Item.backpack.append(self.items.pop(pos))
        print("Backpack:", end=" ", flush=True)
        for i, items in enumerate(Item.backpack, start=1):
            print(items.get_item_name() + ";", end=" ", flush=True)
        print()

    # To Drop an Item from Backpack to Room
    def drop_item(self):
        """
        To Drop an Item from Backpack to Room
        :return:
        """
        if Item.backpack:
            pos = (len(Item.backpack)-1)
            print("Dropping " + Item.backpack[pos].get_item_name())
            self.items.append(Item.backpack.pop(pos))
        else:
            print("You don't have anything!")

    # Add a Character to a Room
    def add_char(self, char):
        """
        Add a Character to a Room
        :param char:
        :return:
        """
        self.chars.append(char)

    # Delete a Character from a Room
    def delete_char(self, char):
        """Delete a Character from a Room"""
        char.delete_char_from_room(self)

    # Get all Characters in a Room
    def get_chars(self):
        """
        Get all Characters in a Room
        :return:
        """
        if self.chars:
            print("Room occupants:", end=" ", flush=True)
            for i, char in enumerate(self.chars, start=1):
                print("(" + str(i) + ") " + char.get_char_name() + ";", end=" ", flush=True)
            print()
        else:
            print("Room occupants: There's no one here!")
