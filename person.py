class Person:
    def __init__(self,canvas, x, y, name = "Name", surname = "Surname", width=130, height=50):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.display_x = x
        self.display_y = y
        self.name = name
        self.surname = surname
        self.width = width
        self.height = height
        self.rect_id = self.canvas.create_rectangle(x, y, x + self.width, y + self.height, fill='lightblue', tags="draggable")
        self.txt_name_id = self.canvas.create_text(x + self.width / 2, y + self.height * 1/ 3, text=name, font=("Arial", 10),
                                          tags="draggable")
        self.txt_surname_id = self.canvas.create_text(x + self.width / 2, y + self.height * 2/ 3, text=surname, font=("Arial", 10),
                                          tags="draggable")
        self.connections = []

    def set_canvas_ids(self, rect_id, txt_name_id, txt_surname_id):
        self.rect_id = rect_id
        self.txt_name_id = txt_name_id
        self.txt_name_id = txt_surname_id

    def check_if_clicked(self, clicked_ids  :set[int]) -> bool:
        if self.rect_id in clicked_ids or self.txt_name_id in clicked_ids or self.txt_surname_id in clicked_ids:
            return True
        return False

    def get_center(self):
        return self.display_x + self.width / 2, self.display_y + self.height / 2

    def move(self, dx, dy):
        self.canvas_move(dx,dy)

        self.x += dx
        self.y += dy
        self.display_x += dx
        self.display_y += dy

    def move_display(self, dx, dy):
        self.canvas_move(dx,dy)

        self.display_x += dx
        self.display_y += dy

    def canvas_move(self,dx,dy):
        self.canvas.move(self.rect_id, dx, dy)
        self.canvas.move(self.txt_name_id, dx, dy)
        self.canvas.move(self.txt_surname_id, dx, dy)

    def reset_display(self):
        self.canvas.coords(self.rect_id, self.x, self.y, self.x + self.width, self.y + self.height )
        self.canvas.coords(self.txt_name_id, self.x + self.width / 2, self.y + self.height *1/ 3)
        self.canvas.coords(self.txt_surname_id, self.x + self.width / 2, self.y + self.height *2/ 3)

        self.display_x = self.x
        self.display_y = self.y

    def add_connection(self, connection):
        self.connections.append(connection)

    def remove_connection(self, connection):
        self.connections.remove(connection)

    def delete_canvas(self):
        self.canvas.delete(self.rect_id)
        self.canvas.delete(self.txt_name_id)
        self.canvas.delete(self.txt_surname_id)

    def edit_name(self, name :str):
        self.name = name
        self.canvas.itemconfig(self.txt_name_id, text=name)

    def edit_surname(self, surname :str):
        self.surname = surname
        self.canvas.itemconfig(self.txt_surname_id, text=surname)


    def get_name_and_surname(self) -> tuple[str, str]:
        return self.name, self.surname

    def check_in_box(self,x,y):
        return self.display_x <= x <= self.display_x + self.width and self.display_y <= y <= self.display_y + self.height