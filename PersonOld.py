class Person(object):
    def __init__(self, id, name, surename, gender, level = 0):
        self.id = id
        self.first_name = name
        self.surename = surename
        self.x, self.y = 0, 0
        self.child_id = []
        self.sibling_id = -1
        self.partner_id = -1
        self.gender = gender
        self.level = level

    def get_name(self):
        return self.first_name + " " + self.surename

    def set_position(self,x,y, offset : tuple = (0,0)):
        if self.gender == 'M':
            self.x = x - offset[0]
        else:
            self.x = x + offset[0]
        self.y = y - offset[1]

    def move_position(self, site, offset):
        if site =='l':
            self.x = self.x - offset[0]
        else:
            self.x = self.x + offset[0]


    def get_position(self):
        return self.x, self.y

    def get_current_window_position(self, index : tuple):
        return self.x + index[0], self.y - index[1]

    def set_child_id(self, new_id):
        self.child_id.append(new_id)

    def get_first_child_id(self):
        return self.child_id[0]
    def get_child_id_list(self):
        return self.child_id

    def set_sibling_id(self, new_id):
        self.sibling_id = new_id

    def get_sibling_id(self):
        return self.sibling_id
    def not_empty_child_id(self):
        return True if len(self.child_id)> 0  else False
if __name__ == '__main__':
    obj = Person('1', 'A', 'A', 'F', 2)
    obj.set_child_id(2)
    # obj.change_position(obj.persons[3],5)
    print(obj.not_empty_child_id())