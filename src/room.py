# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_rooms = []
        self.exits = []
        self.items = {}

    def __str__(self):
        output = f"{self.name}\n{self.description}"
        # for exit in self.exits:
        #     output += f'\nExit to the {exit}'
        return output

    def addItem(self, item_name, item_description):
        self.items[item_name] = item_description

    def removeItem(self, item):
        del self.items[item]

    def getItems(self):
        return self.items

    exits = []
    linked_rooms = []
