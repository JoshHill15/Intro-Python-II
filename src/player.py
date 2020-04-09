# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} has picked up {item}!")

    def remove_item(self, item):
        self.inventory.remove(item)
        print(f"{self.name} has dropped up {item}!")
