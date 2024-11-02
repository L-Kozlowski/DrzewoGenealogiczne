import pandas as pd
from Person import Person

class PersonList(object):
    class PersonID(object):
        def __init__(self):
            self.id = 0

        def next_id(self):
            self.id += 1
            return self.id

    def __init__(self):
        self.persons = []
        self.id = self.PersonID()
        self.personId = self.PersonID()
        self.read_excel()

    def __iter__(self):
        return iter(self.persons)

    def get_person_list(self):
        return self.persons

    def read_excel(self):
        file_path = 'persons.ods'
        df = pd.read_excel(file_path, engine='odf')
        for index, row in df.iterrows():
            row_dict = row.to_dict()
            # print(int(row_dict['ChildID']))

            p = Person(self.personId.next_id(), row_dict['Name'], row_dict['Surename'], row_dict['Gender'])
            p.set_child_id(int(row_dict['ChildID']))
            p.set_sibling_id(int(row_dict['SiblingID']))

            self.persons.append(p)

    def print_persons(self):
        for person in self.persons:
            print(person.id, person.get_name())

    def get_persons_list(self):
        return self.persons

    def add_person(self, name, surename, gender):
        p = Person(self.personId.next_id(), name, surename, gender)
        self.persons.append(p)

    def set_configue(self, screen_width, screen_height):
        self.persons[0].set_position(screen_width//2,  screen_height//2)
        self.set_persons_position((80, 40))

    def set_persons_position(self, offset : tuple = (0,0)):
        for person in self.persons:
            for p in self.persons:
                if person.get_child_id() == p.id:
                    # print(person.get_name() + " znaleziono dziecko: " + p.get_name())
                    if person.gender == 'M':
                        person.set_position(*p.get_position(), (-offset[0], offset[1]))
                    else:
                        person.set_position(*p.get_position(), offset)
                elif person.get_sibling_id() == p.id:
                    person.set_position(*p.get_position(), (2*offset[0], 0))

if __name__ == '__main__':
    obj = PersonList()
    obj.print_persons()