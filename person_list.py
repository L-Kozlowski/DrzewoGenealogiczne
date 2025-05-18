from person import Person
from connection_line import ConnectionLine

class PersonList:
    def __init__(self, canvas):
        self.persons: list[Person] = []
        self.lines: list[ConnectionLine] = []
        self.canvas = canvas
        self.selected_person = None

    def get_persons(self):
        return self.persons

    def get_lines(self):
        return self.lines

    def add_to_persons(self,new_person):
        self.persons.append(new_person)

    def add_person(self, new_person: Person, releted_person: Person, color="black" ):
        self.persons.append(new_person)
        self.connect_persons(new_person, releted_person, color)

    def connect_persons(self, r1: Person, r2: Person, color="black"):
        line = ConnectionLine(self.canvas, r1, r2, color=color)
        self.canvas.tag_lower("line")
        self.lines.append(line)

    def delete_person(self):
        # validation
        if len(self.selected_person.connections) > 1:
            print("To many connections")
        elif len(self.persons) == 1:
            print("You cannot delete last one")
        else:
            # delete person
            self.selected_person.delete_canvas()
            self.persons.remove(self.selected_person)

            # delete connected lines
            for line in self.selected_person.connections:
                line.delete()

    def reset_view(self):
        for person in self.persons:
            person.reset_display()
        self.update_all_lines()

    def update_all_lines(self):
        for line in self.lines:
            line.update()

    def set_selected_person(self, person):
        self.selected_person = person