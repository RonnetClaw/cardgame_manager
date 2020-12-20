class Item():

    discarded_items = []
    backpack = []

    # Initializing an Item
    def __init__(self, item_name, item_type=None):
        """
        Initialize an Item
        :param item_name:
        :param item_type:
        """
        self.item_name = item_name
        self.item_type = item_type

    # BASICS:
    # Set Item name
    def set_item_name(self, item_name):
        """
        Set Item name
        :param item_name:
        :return:
        """
        self.item_name = item_name

    # Get Item name
    def get_item_name(self):
        """
        Get Item name
        :return:
        """
        return self.item_name

    # Set Item type
    def set_item_type(self, item_type):
        """
        Set Item type
        :param item_type:
        :return:
        """
        self.item_type = item_type

    # Get Item type
    def get_item_type(self):
        """
        Get Item type
        :return:
        """
        return self.item_type

    # ITEM, ROOM MANAGEMENT:
    # Add Item to Room
    def add_item_to_room(self, room):
        """
        Add Item to Room
        :param room:
        :return:
        """
        room.items.append(self)

    # Delete Item from Room, move to Discard Pile
    def delete_item_from_room(self, room):
        """
        Delete Item from Room, move to Discard Pile
        :param room:
        :return:
        """
        print(self.get_item_name() + " is deleted from " + room.get_room_name())
        pos = room.items.index(self)
        Item.discarded_items.append(room.items.pop(pos))
