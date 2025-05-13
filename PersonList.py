import pandas as pd
from PersonOld import Person

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
        self.persons_tmp = []
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

            p = Person(self.personId.next_id(), row_dict['Name'], row_dict['Surename'], row_dict['Gender'], row_dict['Level'])
            try:
                if int(row_dict['ChildID']) != -1:
                    p.set_child_id(int(row_dict['ChildID']))
            except ValueError:
                for child_id in row_dict['ChildID'].split(';'):
                    p.set_child_id(int(child_id))

            if int(row_dict['SiblingID']) != -1:
                p.set_sibling_id(int(row_dict['SiblingID']))
            # self.set_persons_position(p, (80,40))

            self.persons.append(p)

    def set_init_position(self, person, new_person, offset):
        if person.id == new_person.get_sibling_id(): # sibling
            if (person.x < 0 and new_person.gender == 'F') or (person.x >= 0 and new_person.gender == 'M'):
                new_person.set_position(*person.get_position(), (-2*offset[0], 0))
            elif (person.x <= 0 and new_person.gender == 'M') or (person.x > 0 and new_person.gender == 'F'):
                new_person.set_position(*person.get_position(), offset=(2*offset[0], 0))

        elif person.id == new_person.get_first_child_id() and new_person.not_empty_child_id(): # parent
            position = person.get_position()
            if len(new_person.get_child_id_list()) > 1:
                    min_x = 0
                    max_x = 0
                    for childid in new_person.get_child_id_list():
                        for person in self.persons:
                            if person.id == childid:
                                if min_x == 0 or min_x > person.get_position()[0]:
                                    min_x = person.get_position()[0]
                                elif min_x == 0 or max_x < person.get_position()[0]:
                                    max_x = person.get_position()[0]
                                print(person.get_name(), 'Sibling sum:',min_x, max_x)
                                break
                    if (person.x < 0 and new_person.gender == 'M') or (person.x > 0 and new_person.gender == 'F'):
                        position = (max_x, position[1])
                    elif (person.x < 0 and new_person.gender == 'F') or (person.x > 0 and new_person.gender == 'M'):
                        position = (min_x, position[1])
            if person.x < 0 and new_person.gender == 'F':
                new_person.set_position(*position, (0,offset[1]))
            elif person.x <= 0 and new_person.gender == 'M':
                new_person.set_position(*position, offset=offset)

            elif person.x > 0 and new_person.gender == 'M':
                new_person.set_position(*position, (0, offset[1]))
            elif person.x >= 0 and new_person.gender == 'F':
                new_person.set_position(*position, offset=offset)


    def print_persons(self):
        for person in self.persons:
            print(person.id, person.get_name(), person.get_position())

    def get_persons_list(self):
        return self.persons

    def add_person(self, name, surename, gender):
        p = Person(self.personId.next_id(), name, surename, gender)
        self.persons.append(p)

    def set_configue(self, screen_width, screen_height):
        # self.persons[0].set_position(screen_width//2,  screen_height//2)
        # self.set_persons_position((80, 40))

        for p in self.persons:
            if p.id == 1:
                self.persons[0].set_position(0,0)
                self.persons_tmp.append(self.persons[0])
            else:
                # self.set_persons_position(p, (80, 40))
                self.set_positions(p, (80, 40))

        # self.print_persons()

    def set_positions(self, new_person, offset):

        for person in self.persons_tmp: # set new position for person
            if new_person.get_sibling_id() != -1:
                if person.id == new_person.get_sibling_id():
                    self.set_init_position(person, new_person, offset)
                    self.persons_tmp.append(new_person)
            elif new_person.get_first_child_id() == person.id:
                self.set_init_position(person, new_person, offset)
                self.persons_tmp.append(new_person)
                break
        print("New position: ", new_person.get_name(), new_person.get_position())

        for person in self.persons_tmp: # change previous person position
            not_last_child = person.not_empty_child_id
            if person.x <= new_person.x and not_last_child and person.id != new_person.id and new_person.x < 0:
                print('Move B: ', person.get_name(), person.get_position())
                person.move_position('l',offset)
                print('Move A:', person.get_name(), person.get_position())
            elif person.x >= new_person.x and not_last_child and person.id != new_person.id and new_person.x > 0:
                print('right')
                print('Move B: ', person.get_name(), person.get_position())
                person.move_position('r',offset)
                print('Move A:', person.get_name(), person.get_position())


if __name__ == '__main__':
    obj = PersonList()
    obj.set_configue(10,10)
    # obj.change_position(obj.persons[3],5)
    obj.print_persons()