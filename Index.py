class Index(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    def turn(self, direction : str):
        if direction == 'left':
            self.x -= 1
        if direction == 'right':
            self.x += 1
        if direction == 'up':
            self.y += 1
        if direction == 'down':
            self.y -= 1

    def get_index(self):
        return self.x, self.y

if __name__ == '__main__':
    idx = Index()
    print(idx.get_index())
    idx.turn('left')
    print(idx.get_index())
