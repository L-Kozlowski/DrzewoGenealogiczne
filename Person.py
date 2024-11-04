class Person(object):
    def __init__(self, id, name, surename, gender, level = 0):
        self.id = id
        self.first_name = name
        self.surename = surename
        self.x, self.y = 0, 0
        self.child_id = -1
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
        self.child_id = new_id

    def get_child_id(self):
        return self.child_id

    def set_sibling_id(self, new_id):
        self.sibling_id = new_id

    def get_sibling_id(self):
        return self.sibling_id
