from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items=["helmet", "knife"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items=["sword"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items=["feather, fish"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items=["flower"]),
}


# Link rooms together

room['outside'].n_to = "foyer"
room['foyer'].s_to = "outside"
room['foyer'].n_to = "overlook"
room['foyer'].e_to = "narrow"
room['overlook'].s_to = "foyer"
room['narrow'].w_to = "foyer"
room['narrow'].n_to = "treasure"
room['treasure'].s_to = "narrow"

# room['outside'].n_to = "room['foyer']"
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#
print("Welcome to the Adventure Game!")
# Make a new player object that is currently in the 'outside' room.
player = Player("josh", "outside")
# input("Enter your name here: ")
print(f"\nHello {player.name}! You'll be starting off in the room Outside Cave Entrance, Navigate with your keyboard to move to different rooms!")
print(f"\nGuide: {room[player.current_room].description}")
print("--------------------------------------------------------------------------------------------------")

userInput = input("""   ------- COMMANDS -------
-input [n] to move North.
-input [s] to move South.
-input [w] to move West.
-input [e] to move East.
-input [q] to quit the game.
-input [c] to review the rules of the game again.
-input [i] to see your inventory.
-input [get "item_name"] to grab an item in a particular room.
-input [drop "item_name"] to drop an item in a particular room.

----------------------------
""")
# Write a loop that:
while userInput != "q":
    userInput = userInput.split()
    if len(userInput) == 0:
        print("Input a command into the terminal, or press q to quit\n")
    elif len(userInput) == 1:
        userInput = userInput[0]
        if userInput == "n":
            if room[player.current_room].n_to == None:
                # if theres no room to the north
                print("No room exists to the North")
            else:
                player.current_room = room[player.current_room].n_to
                print("\nLocation: " + room[player.current_room].name)
                print(
                    f"Items: {room[player.current_room].items}")
                print("Guide: " + room[player.current_room].description)
        elif userInput == "s":
            if room[player.current_room].s_to == None:
                # if theres no room to the south
                print("No room exists to the South")
            else:
                player.current_room = room[player.current_room].s_to
                print("\nLocation: " + room[player.current_room].name)
                print(
                    f"Items: {room[player.current_room].items}")
                print("Guide: " + room[player.current_room].description)
        elif userInput == "e":
            if room[player.current_room].e_to == None:
                # if theres no room to the east
                print("No room exists to the East")
            else:
                player.current_room = room[player.current_room].e_to
                print("\nLocation: " + room[player.current_room].name)
                print(
                    f"Items: {room[player.current_room].items}")
                print("Guide: " + room[player.current_room].description)
        elif userInput == "w":
            if room[player.current_room].w_to == None:
                # if theres no room to the west
                print("No room exists to the West")
            else:
                player.current_room = room[player.current_room].w_to
                print("\nLocation: " + room[player.current_room].name)
                print(
                    f"Items: {room[player.current_room].items}")
                print("Guide: " + room[player.current_room].description)
        elif userInput == "c":
            print("""   ------- COMMANDS -------
-input [n] to move North.
-input [s] to move South.
-input [w] to move West.
-input [e] to move East.
-input [q] to quit the game.
-input [r] to review the rules of the game again.
-input [i] to see your inventory.
-input [get "item_name"] to grab an item in a particular room.
-input [drop "item_name"] to drop an item in a particular room.

----------------------------
            """)
        elif userInput == "i":
            print(player.inventory)
        else:
            print("Invalid Selection. Type a cardinal direction or input q to quit\n")
            print("Location: " + room[player.current_room].name)
            print(
                f"Items: {room[player.current_room].items}")
            print("Guide: " + room[player.current_room].description)
    else:
        if len(userInput) != 2:
            print(
                """Invalid Selection. Try typing "get "item_name" or input q to quit\n""")
        elif userInput[0] == "get":
            if room[player.current_room].items == []:
                print("There are no items in this room to grab!")
            else:
                # has items
                if userInput[1] in room[player.current_room].items:
                    player.add_item(userInput[1])
                    room[player.current_room].remove_item(userInput[1])
                else:
                    print(
                        f"Oh No! There doesn't seem to be a {userInput[1]} this room!")
        elif userInput[0] == "drop":
            if player.inventory == []:
                print("You have no Items to drop in your Inventory!")
            else:
                if userInput[1] in player.inventory:
                    room[player.current_room].add_item(userInput[1])
                    player.remove_item(userInput[1])
                else:
                    print(
                        f"Oh No! There doesn't seem to be {userInput[1]} in your inventory!")
    userInput = input("input a command to continue on your adventure!: ")


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
