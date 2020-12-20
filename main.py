from room import Room
from item import Item
from character import Character, Enemy
from rpginfo import RPGInfo

spooky_castle = RPGInfo("The Spooky Castle!")
spooky_castle.welcome()

RPGInfo.info()

# Creating Room - classic style
dungeon = Room("Dungeon")
dungeon.set_room_desc("Oh, it's dark in here!")

# Creating Room - modern style
boss_lair = Room("Boss Lair", "It's scary down here!")
stairwell = Room("Stairwell", "huff, puff... Are we there yet?")
hallway = Room("Hallway", "It's very bright in here!")

# Linked Rooms together
dungeon.link_room(boss_lair, "Left")
dungeon.link_room(stairwell, "Right")
stairwell.link_room(hallway, "Up")

# Creating Item - classic style
weapon = Item("Silver Dagger")
weapon.set_item_type("Weapon")

# Creating Item - compact style
spell = Item("Purge", "Spell")
gold = Item("Gold", "Treasure")

# Add Items to Room - classic way
weapon.add_item_to_room(hallway)
spell.add_item_to_room(dungeon)

# Add Item to Room - by way of room
boss_lair.add_item(gold)

# Adding a test Item to Backpack
hp_potion = Item("HP Potion", "Potion")
Item.backpack.append(hp_potion)

# Adding a character
soldier = Character("Soldier", "May I help?")
demon1 = Enemy("Darkling", "Aarrgh!")
demon_king = Enemy("Demon King", "Aarrgh!")

# Setting Weakness to Enemy character
demon_king.set_weakness(spell)
demon1.set_weakness(weapon)

# Adding Characters to Room - 2 ways to do it.
demon1.add_char_to_room(dungeon)
boss_lair.add_char(demon_king)
soldier.add_char_to_room(hallway)


current_room = hallway

while True:
    current_room.get_room_details()
    command = input("Enter command (move, pick, drop, talk, fight, exit): ")
    if command.lower() == "move":
        current_room.get_links()
        print()
        direction = input("Enter direction (left/right/up/down): ")
        if direction.lower() in ("left", "right", "up", "down"):
            print("Going " + direction.lower() + "...")
            current_room = current_room.move(direction.capitalize())
            input("__Press any key!__")
    elif command.lower() == "pick":
        current_room.pick_item()
        input("__Press any key!__")
    elif command.lower() == "exit":
        print("The game has ended!")
        input("__Press any key!__")
        break
    elif command.lower() == "drop":
        current_room.drop_item()
        input("__Press any key!__")
    elif command.lower() == "talk":
        if current_room.chars:
            for chars in current_room.chars:
                chars.talk()
                input("__Press any key!__")
        else:
            print("There's no one here to talk!")
            input("__Press any key!__")
    elif command.lower() == "fight":
        if current_room.chars:
            for chars in current_room.chars:
                chars.fight()
                input("__Press any key!__")
        else:
            print("There's no one here to fight!")
            input("__Press any key!__")
    else:
        print("Wrong command!")
        print("Type 'Exit' to quit!")
        continue

print()
RPGInfo.credits()
