# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_rooms = []
        self.exits = []

    def __str__(self):
        output = f"{self.name}\n{self.description}"
        # for exit in self.exits:
        #     output += f'\nExit to the {exit}'
        return output

    exits = []
    linked_rooms = []

    # def n_to(self, room):
    #     self.exits.append('n')
    #     print(self)

    # def s_to(self, room):
    #     self.exits.append('s')

    # def e_to(self, room):
    #     self.exits.append('e')

    # def w_to(self, room):
    #     self.exits.append('w')
