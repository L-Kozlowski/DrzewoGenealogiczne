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
            p.set_child_id(int(row_dict['ChildID']))
            p.set_sibling_id(int(row_dict['SiblingID']))
            # self.set_persons_position(p, (80,40))

            self.persons.append(p)

    def set_init_position(self, person, new_person, offset):
        if person.id == new_person.get_child_id() and new_person.get_child_id() != -1:
            if person.x < 0 and new_person.gender == 'F':
                new_person.set_position(*person.get_position(), (0,offset[1]))
            elif person.x <= 0 and new_person.gender == 'M':
                new_person.set_position(*person.get_position(), offset=offset)

            elif person.x > 0 and new_person.gender == 'M':
                new_person.set_position(*person.get_position(), (0, offset[1]))
            elif person.x >= 0 and new_person.gender == 'F':
                new_person.set_position(*person.get_position(), offset=offset)

    def adjust_position_after_add_new_person(self, person, new_person,offset ,site):
        if site == 'l':
            site_condition= person.x <= new_person.x <= 0
            of = (-offset[0], 0)
        else:
            site_condition = 0 < new_person.x <= person.x
            of = (offset[0], 0)


        if (
                person.id == new_person.get_child_id and
                person.id != new_person.id and
                person.level <= new_person.level and
                person.get_child_id() != -1 and site_condition):   # left
            print(site,person.get_name(), person.get_position(), new_person.get_name(),new_person.get_position())
            # person.set_position(*person.get_position(), offset=(offset[0], 0))
            person.move_position(site,offset)
            # zmiana miejsca nowej osoby, poniewaz osoba z której została stworzona została przsunięta
            if person.id == new_person.get_child_id() and new_person.get_child_id() != -1:
                print(new_person.get_name())
                new_person.set_position(*new_person.get_position(), offset=of)

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
                self.persons[0].set_position(screen_width//2,  screen_height//2)
                self.persons[0].set_position(0,0)
                self.persons_tmp.append(self.persons[0])
            else:
                # self.set_persons_position(p, (80, 40))
                self.set_positions(p, (80, 40))

        # self.print_persons()

    def set_positions(self, new_person, offset):

        for person in self.persons_tmp:
            if new_person.get_child_id() == person.id:
                self.set_init_position(person, new_person, offset)
                self.persons_tmp.append(new_person)
        print("New position: ", new_person.get_name(), new_person.get_position())

        for person in self.persons_tmp:
            not_last_child = person.get_child_id() != -1
            if person.x <= new_person.x and not_last_child and person.id != new_person.id and new_person.x < 0:
                print('Move B: ', person.get_name(), person.get_position())
                person.move_position('l',offset)
                print('Move A:', person.get_name(), person.get_position())
            elif person.x >= new_person.x and not_last_child and person.id != new_person.id and new_person.x > 0:
                print('right')
                print('Move B: ', person.get_name(), person.get_position())
                person.move_position('r',offset)
                print('Move A:', person.get_name(), person.get_position())


    def set_persons_position(self, new_person, offset : tuple = (0,0)):
        for person in self.persons:
            self.set_init_position(person, new_person, offset)
            self.adjust_position_after_add_new_person(person, new_person, offset, 'l')
            self.adjust_position_after_add_new_person(person, new_person, offset, 'r')

        # for person in self.persons:
        #     for p in self.persons:
        #         if person.get_child_id() == p.id:
        #             # print(person.get_name() + " znaleziono dziecko: " + p.get_name())
        #             if person.gender == 'M':
        #                 person.set_position(*p.get_position(), (-offset[0], offset[1]))
        #             else:
        #                 person.set_position(*p.get_position(), offset)
        #         elif person.get_sibling_id() == p.id:
        #             person.set_position(*p.get_position(), (2*offset[0], 0))

    def new_pos(self, person, person2, offset):
        if person.gender == 'M':
            person.set_position(*person2.get_position(), (-offset[0], offset[1]))
        else:
            person.set_position(*person2.get_position(), offset)

    # def change_position(self, person : Person, position):
    #     position -=1
    #     print('wejscie:', person.get_name(), 'pozycja:', person.get_position())
    #
    #     if person.get_child_id() != -1:
    #         self.change_position(self.persons[person.get_child_id()-1],position)
    #         self.new_pos(person, (10, 0))
    #     print('wyjscie: ', person.get_name(), 'pozycja:', person.get_position())


if __name__ == '__main__':
    obj = PersonList()
    obj.set_configue(10,10)
    # obj.change_position(obj.persons[3],5)
    obj.print_persons()