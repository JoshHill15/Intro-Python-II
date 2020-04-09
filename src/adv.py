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
print(f"\nHello {player.name}! You'll be starting off in the room {player.current_room}, Navigate with your keyboard to move to different rooms!")
print(f"\nGuide: {room[player.current_room].description}")
print("-----------------------------------------------------------------------------------------------------------------")

userInput = input("""   ------- RULES -------
-press [n] to move North,
-press [s] to move South,
-press [w] to move West,
-press [e] to move East,
-press [q] to quit the game.
----------------------------
""")

# Write a loop that:
while userInput != "q":
    if userInput == "n":
        if room[player.current_room].n_to == None:
            # if theres no room to the north
            print("No room exists to the North")
        else:
            player.current_room = room[player.current_room].n_to
            print("Location: " + room[player.current_room].name)
            print(
                f"Items: {room[player.current_room].items}")
            print("Guide: " + room[player.current_room].description)
    elif userInput == "s":
        if room[player.current_room].s_to == None:
            # if theres no room to the south
            print("No room exists to the South")
        else:
            player.current_room = room[player.current_room].s_to
            print("Location: " + room[player.current_room].name)
            print(
                f"Items: {room[player.current_room].items}")
            print("Guide: " + room[player.current_room].description)
    elif userInput == "e":
        if room[player.current_room].e_to == None:
            # if theres no room to the east
            print("No room exists to the East")
        else:
            player.current_room = room[player.current_room].e_to
            print("Location: " + room[player.current_room].name)
            print(
                f"Items: {room[player.current_room].items}")
            print("Guide: " + room[player.current_room].description)
    elif userInput == "w":
        if room[player.current_room].w_to == None:
            # if theres no room to the west
            print("No room exists to the West")
        else:
            player.current_room = room[player.current_room].w_to
            print("Location: " + room[player.current_room].name)
            print(
                f"Items: {room[player.current_room].items}")
            print("Guide: " + room[player.current_room].description)
    else:
        print("Invalid Selection. Type a cardinal direction or press q to quit\n")
        print("Location: " + room[player.current_room].name)
        print(
            f"Items: {room[player.current_room].items}")
        print("Guide: " + room[player.current_room].description)

    userInput = input("""   -----RULES-----
-press [n] to move North,
-press [s] to move South,
-press [w] to move West,
-press [e] to move East,
-press [q] to quit the game.
----------------------------
""")


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
