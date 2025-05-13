class ConnectionLine:
    def __init__(self, canvas, rect1, rect2, color="black"):
        self.canvas = canvas
        self.rect1 = rect1
        self.rect2 = rect2
        self.color = color

        self.l1 = canvas.create_line(0, 0, 0, 0, width=2, fill=color, tags="line")
        self.l2 = canvas.create_line(0, 0, 0, 0, width=2, fill=color,tags="line")
        self.l3 = canvas.create_line(0, 0, 0, 0, width=2, fill=color, tags="line")
        self.line_ids = [self.l1,self.l2,self.l3]
        self.rect1.add_connection(self)
        self.rect2.add_connection(self)

        self.update()

    def update(self):
        x1, y1 = self.rect1.get_center()
        x2, y2 = self.rect2.get_center()
        mid_y = (y1 + y2) / 2

        self.canvas.coords(self.l1, x1, y1, x1, mid_y)
        self.canvas.coords(self.l2, x1, mid_y, x2, mid_y)
        self.canvas.coords(self.l3, x2, mid_y, x2, y2)

    def delete(self):
        for lid in self.line_ids:
            self.canvas.delete(lid)
        self.rect1.remove_connection(self)
        self.rect2.remove_connection(self)
